
<img src="Images/CartmanLogo.PNG"  style="border: 0;"/>


## Abstract

Understanding gene regulation requires exploring complex genomic sequence structures beyond individual transcription factor motifs. **CARTMAN** (Co-occurrence Analysis of Repeating Transcription-factor Motifs And Networks) is a software tool that performs discovery and quantification of motif co-occurrences within regulatory sequences and enables downstream differential analysis of motif complexes across distinct experimental conditions. Unlike high-complexity machine learning approaches, CARTMAN offers straightforward and interpretable measures minimizing computational overhead and user background requirements. CARTMAN’s motif co-occurrence constructs parallel the simplicity and interpretability of motifs as co-occurrence of individual nucleotides, representing a logical and natural progression of well-established genomic motif discovery tools like [HOMER](http://homer.ucsd.edu/homer/) and [FIMO](https://meme-suite.org/meme/tools/fimo).


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

The data files used in this example are derived from the following paper:

Seidman JS, Troutman TD, Sakai M, Gola A, Spann NJ, Bennett H, Bruni CM, Ouyang Z, Li RZ, Sun X, Vu BT, Pasillas MP, Ego KM, Gosselin D, Link VM, Chong L, Evans RM, Thompson BM, McDonald JG, Hosseini M, Witztum JL, Germain RN, Glass CK. Niche-Specific Reprogramming of Epigenetic Landscapes Drives Myeloid Cell Diversity in Nonalcoholic Steatohepatitis. Immunity. 2020 Apr 28;S1074-7613(20)30159-X. doi: 10.1016/j.immuni.2020.04.001. [PMID: 32362324](https://pubmed.ncbi.nlm.nih.gov/32362324/)

Full datase on GEO: [GSE128338](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE128338)

The notebook example uses the following peak and motif files derived from this dataset:

1. Peak files:
   - `KCH_H3K_FC2_1000_w200.txt`
   - `KCN_H3K_FC2_1000_w200.txt`

2. Target motif list file:
   - `KCH_VS_KCN_w400_L70.motifs`

Data files are located in the `data` directory.
