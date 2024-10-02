# CARTMAN Project v0.1 - 2024
# The most up-to-date version of this code can be found at:
# https://github.com/psaisan/CARTMAN
#
# Copyright (c) 2024 P. Saisan
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions must retain this copyright notice, conditions, and disclaimer.
# 2. Neither the name of University of California nor the names of its contributors 
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# This software is provided by the copyright holders and contributors "AS IS"
# and any express or implied warranties, including, but not limited to, the
# implied warranties of merchantability and fitness for a particular purpose
# are disclaimed. In no event shall the copyright owner or contributors be
# liable for any direct, indirect, incidental, special, exemplary, or
# consequential damages arising in any way out of the use of this software.
#
# IMPORTANT NOTICE: This is developmental code (v0.0). Use with caution.
# Not all cases tested. Check GitHub for updates and report issues there.

import os
import pandas as pd
import matplotlib.pyplot as plt
from upsetplot import plot
import itertools
from motif_utils import read_motif_headers
from homer_utils import get_motif_count
from combination_utils import all_possible_combinations33, transform_combinations_to_matrix

def peak_motif_sets(
    peak_file,
    genome,
    motif_list_file,
    output_file=None,
    Motif_recount=False,
    seperate_duplicates=False,
    min_motif_set_count=0,
    min_subset_count=0
):
    """
    Process motif analysis and generate an UpSet plot and normalized bar graphs as image files.

    Parameters:
        peak_file (str): Path to the peak file.
        genome (str): Genome reference.
        motif_list_file (str): Path to the motif list file.
        output_file (str, optional): Base path for saving the plots. The function appends
                                     '_upset.png' and '_bar.png' to save distinct plots.
        Motif_recount (bool, optional): Whether to force motif recount. Defaults to False.
        seperate_duplicates (bool, optional): Whether to separate duplicates. Defaults to False.
        min_motif_set_count (int, optional): Minimum number of motifs in a set. Defaults to 0.
        min_subset_count (int, optional): Minimum subset size for plotting. Defaults to 0.

    Returns:
        tuple: A tuple containing the sorted data and the binary table.
    """
    headers = read_motif_headers(motif_list_file)
    motif_count_table, motif_count_file = get_motif_count(
        peak_file, genome, motif_list_file, force=Motif_recount
    )

    formatted_table = motif_count_table.iloc[:, -len(headers):].T
    formatted_table.columns = motif_count_table.iloc[:, 0]
    formatted_table.columns.name = 'PeakID'
    formatted_table.index = headers

    if seperate_duplicates:
        formatted_table = formatted_table.T
        for item in subset_motifs:
            condition = formatted_table[item] > 2
            formatted_table.loc[condition, item] = 0
            new_col = f'{item}_3+'
            formatted_table[new_col] = 1 * condition
        formatted_table = formatted_table.T
        headers = formatted_table.index

    binary_table = (formatted_table >= 0.5).astype(int)
    df = binary_table.T
    df_sorted = df.sort_values(by='PeakID')

    if len(headers) == len(df.columns):
        df.columns = headers
    else:
        print("Error: The number of headers does not match the number of columns in the DataFrame.")

    df_upset = df.groupby(list(df.columns)).size().reset_index(name='count')
    df_upset['num_motifs'] = df_upset.drop('count', axis=1).sum(axis=1)
    filtered_df = df_upset[df_upset['num_motifs'] > min_motif_set_count]
    filtered_df.set_index(df.columns.tolist(), inplace=True)
    upset_data = filtered_df['count']

    save_as_images = False
    image_extensions = ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']

    if output_file:
        _, ext = os.path.splitext(output_file)
        ext = ext.lower()
        if ext in image_extensions:
            save_as_images = True
            image_base = os.path.splitext(output_file)[0]
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
        else:
            print(f"Unsupported output file extension: {ext}. Plots will not be saved.")

    fig_upset = plt.figure(figsize=(20, 20), constrained_layout=True)
    plot(
        upset_data,
        fig=fig_upset,
        orientation="horizontal",
        show_counts=True,
        min_subset_size=min_subset_count,
        sort_categories_by=None
    )

    title_txt = (
        f'Set intersections: [Membership > {min_motif_set_count}] '
        f'[Counts > {min_subset_count}]\n'
        f'PEAKS: [{peak_file}]\n'
        f'MOTIFS: [{motif_list_file}]\n'
    )
    plt.title(title_txt, fontsize=16)

    if save_as_images:
        upset_image_path = f"{image_base}_upset.png"
        fig_upset.savefig(upset_image_path, bbox_inches="tight")

    sets = {name: set(df[df[col] > 0].index) for name, col in zip(headers, df.columns)}
    membership_df = pd.DataFrame(
        {name: df.index.isin(indices) for name, indices in sets.items()}
    )

    all_combinations = list(
        itertools.chain.from_iterable(
            itertools.combinations(headers, r) for r in range(1, len(headers) + 1)
        )
    )
    ordered_combinations = sorted(all_combinations, key=lambda x: (len(x), x))

    membership_matrix = {
        ','.join(comb): df[list(comb)].all(axis=1) for comb in ordered_combinations
    }
    membership_df = pd.DataFrame(membership_matrix)
    memberships = membership_df.apply(lambda row: list(membership_df.columns[row]), axis=1)
    intersections = memberships.value_counts()

    upset_data1 = all_possible_combinations33(df, min_set_count=min_motif_set_count)

    upset_data1.index = pd.MultiIndex.from_tuples(
        [
            (len(x.split(',')), tuple(sorted(x.split(','))))
            for x in upset_data1.index
        ],
        names=['Cardinality', 'Motifs']
    )
    upset_data1 = upset_data1[
        upset_data1.index.get_level_values('Cardinality') >= min_motif_set_count
    ]
    upset_data1 = upset_data1.sort_index(ascending=False)
    upset_data1.index = [', '.join(motifs) for _, motifs in upset_data1.index]

    sorted_data = upset_data1.sort_values(ascending=True).tail(50)
    total_sum = len(df)
    binary_matrix = transform_combinations_to_matrix(sorted_data, peak_file)
    sorted_binary_matrix = binary_matrix.sort_values(by='Count', ascending=False)
    sorted_data = (sorted_data / total_sum * 10000).astype(int) / 100

    fig_bar = plt.figure(figsize=(20, 30), constrained_layout=True)
    ax = sorted_data.plot(kind='barh', color='green', ax=plt.gca())
    plt.title(
        f'PEAKS [{total_sum}] : {peak_file}\n'
        f'MOTIFS: [{motif_list_file}]',
        fontsize=16
    )
    ax.set_ylabel(
        'Top 50 co-occurring motif groups with # of motifs >= '
        f'{min_motif_set_count}'
    )
    ax.set_xlabel('Co-occurrences (as % ratio of total peaks)')

    for i, (value, index) in enumerate(zip(sorted_data, sorted_data.index)):
        ax.text(
            value,
            i,
            f' {value}, {round(total_sum * value / 100 + 0.5)}',
            va='center',
            ha='left',
            color='black'
        )

    if save_as_images:
        bar_image_path = f"{image_base}_bar.png"
        fig_bar.savefig(bar_image_path, bbox_inches="tight")

    return_table = binary_table.T
    return_data = sorted_data

    return return_data, return_table
