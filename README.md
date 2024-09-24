
<img src="Images/overview.PNG"  style="border: 0;"/>


## Abstract

Understanding gene regulation requires exploring complex genomic sequence structures beyond individual transcription factor motifs. **CARTMAN** (Co-occurrence Analysis of Repeating Transcription-factor Motifs And Networks) is a software tool that enables the discovery and quantification of motif co-occurrences within regulatory sequences and performs differential analysis of motif complexes across distinct experimental conditions. Unlike high-complexity machine learning approaches, CARTMAN offers straightforward and interpretable measures minimizing computational overhead and user background requirements. CARTMAN’s motif co-occurrence constructs parallel the simplicity and interpretability of motifs as co-occurance of individual nucleotides, representing a logical and natural progression of well-established genomic motif discovery tools like HOMER and FIMO.

## Citation

Saisan, P., & Glass, C. (2024). **CARTMAN: Co-occurrence Analysis of Repeating Transcription-factor Motifs And Networks** (Version 1.0) [Computer software]. GitHub. Retrieved from [https://github.com/psaisan/CARTMAN](https://github.com/psaisan/CARTMAN)

### BibTeX Entry

```bibtex
@misc{saisan2024cartman,
  author       = {Saisan, P. and Glass, C.},
  title        = {CARTMAN: Co-occurrence Analysis of Repeating Transcription-factor Motifs And Networks},
  year         = {2024},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/psaisan/CARTMAN}},
  version      = {1.0},
}
```


## Features

- **Motif Co-occurrence Table Generation:** Given a set of target motifs file and a genomic peaks file, CARTMAN constructs and quantifies all possible motif combinations found within the genomic peaks. 
- **Differential Analysis:** Compares motif co-occurrence between two peak sets to identify significant differences.
- **Result Integration:** Outputs normalized counts and significance levels and a number of different visualizations of the motif co-occurances in peak files.

---

## Installation

### Prerequisites

- **Python 3.7+**
- **HOMER Suite:** Ensure HOMER is installed and accessible in your system's PATH.

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/psaisan/CARTMAN.git
   cd CARTMAN
   
---

