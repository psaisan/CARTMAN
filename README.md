
<img src="Images/CartmanLogo.PNG"  style="border: 0;"/>


## Abstract

Uncovering functional relationships between the information content in regulatory sequences and gene expression in cells requires exploring complex genomic sequence structures beyond individual transcription factor motifs. **CARTMAN** (Co-occurrence Analysis of Repeating Transcription-factor Motifs And Networks) is a tool that performs discovery and quantification of motif co-occurrences within regulatory sequences and enables downstream differential analysis of motif complexes across distinct experimental conditions. In contrast to high-complexity machine learning approaches that produce indirect black boxed inferences, CARTMAN produces simple interpretable measures with minimal computational overhead and user background requirement. CARTMAN builds directly on the output of tools like HOMER and FIMO, with motif co-occurrence constructs paralleling the simplicity of motifs as co-occurrence of individual nucleotides. As such, it functions as a natural progression to motif discovery tools.


## Citation   

If you use CARTMAN in your work, please reference it as follows:

Saisan, P., & Glass, C. (2024). CARTMAN: Co-occurrence analysis of repeating transcription-factor motifs and networks (Version 0.1) [Computer software]. GitHub. https://github.com/psaisan/CARTMAN

### BibTeX Entry

```bibtex
@misc{saisan2024cartman,
  author       = {Saisan, P. and Glass, C.},
  title        = {CARTMAN: Co-occurrence Analysis of Repeating Transcription-factor Motifs And Networks},
  year         = {2024},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/psaisan/CARTMAN}},
  version      = {0.1},
}
```

## Installation

### Prerequisites

- **Python 3.7+**
- **HOMER Suite:** Ensure HOMER is installed and accessible in your system's PATH.

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/psaisan/CARTMAN.git
   cd CARTMAN
   
# Example Notebook

[View the CARTMAN Example Notebook](./Notebooks/CARTMAN_Example.ipynb)


## Data Source

The data used in this example is from a 2020 study, [Seidman et al, 2020](https://pubmed.ncbi.nlm.nih.gov/32362324/), looking at epigenomic changes in the immune system cells (Kupffer) as they undergo a diet induced transformation.

1. Peak file1: Regulatory DNA regions active in HEALTHY Kupffer cells 

**`KCH_H3K_FC2_1000_w200.txt`** 

2. Peak file2: Regulatory DNA regions active  in [MASH](https://en.wikipedia.org/wiki/Metabolic_dysfunction%E2%80%93associated_steatotic_liver_disease) transformed Kupffer cells 

**`KCN_H3K_FC2_1000_w200.txt`** 

3. Target motif list file: Subset of HOMER identified motifs found in HEALTHY and MASH Kupffer cells 
   
**`KCH_VS_KCN_w400_L70.motifs`**

Full datase on GEO: [GSE128338](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE128338)


