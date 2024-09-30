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

def get_motif_count(peak_file, genome, motif_file, force=False):
    """Get motif count using HOMER annotatePeaks."""
    base_file = os.path.splitext(os.path.basename(peak_file))[0]
    motif_base_file = os.path.splitext(os.path.basename(motif_file))[0]
    
    base_path = os.path.dirname(os.path.abspath(peak_file))
    
    motif_count_file = os.path.join(base_path, f"motifCount_counts_{base_file}_{motif_base_file}.txt")
    print('Motif_Count_File=', motif_count_file, 'Force=', force)
    command = f'annotatePeaks.pl {peak_file} {genome} -cpu 12 -noann -nogene -m {motif_file} -nmotifs > {motif_count_file}'
    
    if not os.path.exists(motif_count_file):
        print('FILE DOES NOT EXIST: ', motif_count_file)
    
    if not os.path.exists(motif_count_file) or force:
        print(f'{command}')
        print('Generating ' + motif_count_file)
        os.system(command)
    else:
        print(f'** Loading ** ' + motif_count_file)

    return pd.read_table(motif_count_file, sep="\t"), motif_count_file
