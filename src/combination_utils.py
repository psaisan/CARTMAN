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

import pandas as pd
import itertools
from collections import defaultdict

def all_possible_combinations33(df, min_set_count=0):
    motifs = df.columns.tolist()
    combination_counts = {}
    none_present_count = df.eq(0).all(axis=1).sum()
    combination_counts['0_Set'] = none_present_count

    for r in range(1, len(motifs) + 1):
        for comb in itertools.combinations(motifs, r):
            comb_list = list(comb)
            if len(comb_list) >= min_set_count:
                selected_motifs = df[comb_list].all(axis=1)
                non_selected_motifs = df.drop(comb_list, axis=1, errors='ignore').eq(0).all(axis=1)
                exact_match_mask = selected_motifs & non_selected_motifs
                count = exact_match_mask.sum()
                combination_key = ','.join(comb)
                combination_counts[combination_key] = count
    
    return pd.Series(combination_counts)

def transform_combinations_to_matrix(series, peak_file):
    motifs = set()
    for combo in series.index:
        motifs.update(motif.strip() for motif in combo.split(','))
    
    motif_list = sorted(list(set(motifs)))
    peak_data = pd.read_csv(peak_file, sep='\t')
    total_sum = len(peak_data)
    
    data = {motif: [] for motif in motif_list}
    data['Count'] = []
    data['Norm_Count'] = []
    data['Motif Subset'] = []
    data[f'code-{peak_file}'] = []
    
    for combo, count in series.items():
        current_row = {motif: 0 for motif in motif_list}
        current_row['Count'] = count
        current_row['Norm_Count'] = count / total_sum
        current_row['Motif Subset'] = ','.join(sorted(combo.split(',')))
        binary_code = 0

        for motif in motif_list:
            binary_code <<= 1
            if motif in [motif.strip() for motif in combo.split(',')]:
                current_row[motif] = 1
                binary_code |= 1

        current_row[f'code-{peak_file}'] = binary_code
        for key, value in current_row.items():
            data[key].append(value)

    return pd.DataFrame(data)

def calculate_all_motif_co_occurrences(df, max_distance):
    category_counts = defaultdict(int)
    original_motifs = df.columns[1:].tolist()
    motif_columns = {motif: idx for idx, motif in enumerate(original_motifs)}
    
    binary_matrix = []
    peak_names = []
    
    for _, row in df.iterrows():
        co_occurrences = find_co_occurring_motifs(row[1:], max_distance)
        
        if co_occurrences:
            base_peak_id = row[0].rsplit('-', 1)[0]
            start_index = int(row[0].rsplit('-', 1)[1])
            
            for k, occurrence in enumerate(co_occurrences):
                binary_row = [0] * len(original_motifs)
                for motif in occurrence:
                    if motif in motif_columns:
                        binary_row[motif_columns[motif]] = 1
                category_counts[frozenset(occurrence)] += 1
                
                peak_id = f"{base_peak_id}-{start_index + k}"
                binary_matrix.append(binary_row)
                peak_names.append(peak_id)
    
    binary_df = pd.DataFrame(binary_matrix, columns=original_motifs)
    binary_df.insert(0, 'PeakID', peak_names)
    
    return binary_df, category_counts

# Note: The find_co_occurring_motifs function is not defined in the provided code.
# You may need to implement this function separately or import it from another module.
