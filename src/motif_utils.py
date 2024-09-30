import re
import os
import pandas as pd

def read_motif_headers(motif_file):
    """Read headers from a motif file to extract motif names from header lines."""
    if is_denovo_motif_file(motif_file):
        print('DENOVO HOMER')
        return read_motif_headers_homer(motif_file)
    else:
        print('Not DEVONVO HOMER')
        return read_motif_headers_jaspar(motif_file)   

def is_denovo_motif_file(filename):
    """
    Reads a file and checks if any header lines starting with '>' contain "BestGuess:".

    :param filename: str, the path to the file to be read
    :return: bool, True if any header line contains "BestGuess:", otherwise False
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith('>') and "BestGuess:" in line:
                    return True
        return False
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def read_motif_headers_jaspar(motif_file):
    """Read headers from a motif file to extract motif names from header lines."""
    pattern = r'^>(\w+)\t'
    motif_names = []
    
    with open(motif_file, 'r') as file:
        for line in file:
            if line.startswith('>'):  # Check if the line is a header
                match = re.match(pattern, line)
                if match:
                    motif_names.append(match.group(1))  # Add the motif name to the list
    
    print(motif_names)
    return motif_names

def read_motif_headers_homer(motif_file):
    """Read headers from a motif file to extract motif names."""
    pattern = r"BestGuess:([^/]+)"
    with open(motif_file, 'r') as file:
        headers = [line.strip() for line in file if line.startswith('>')]
 
    names = []
    for item in headers:
        names.extend(re.findall(pattern, item))
 
    return names
