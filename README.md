# Lung aging analysis
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/386061763.svg)]()
- [Getting Started](#getting-started)
  * [1. Introduction](#1-introduction)
  * [2. Installation](#2-installation)
    + [2.1 Environment set-up](#21-environment-set-up)
      - [Windows](#windows)
      - [Linux](#linux)
      - [MacOS](#macos)
      - [Next steps](#next-steps)
  * [3. Datasets](#3-datasets)
  * [4. Analyses](#4-analysis)
- [Contact](#contact)
- [Citation](#citation)
- [Copyright](#copyright)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>
# Getting Started
## 1 Introduction
This repository includes jupyter notebooks for reproducing the analysis results presented in the manuscript.

![Alt text](img/fig1_flow.png?raw=true "flowchart")

## 2 Installation
We provide conda environment files to install all necessary packages for users interested in running the analyses in the manuscript. Clone this repository and under the root folder of the repository, you can find `lung_aging.yml` and `HLCA_mapping_env.yml`, where the former is for running most of the analyses and reproducing figures in the manuscript and the latter is for running cell type label transfer between query dataset and the HLCA dataset. You may install this two environments by
```bash
conda env create -f lung_aging.yml
conda env create -f HLCA_mapping_env.yml
```
You will then be able to access all required packages by loading these environments in your jupyter notebook.

## 3 Datasets
Run script `step0_download_data_and_prepare.py` to download all datasets analyzed in the manuscript. The datasets will be downloaded into the folder `data/` under the root folder of this repository. 

## 4 Analyses
The analyses can be performed in the sequential order specified by the prefix "stepX_" of each script file.

# Contact
Contact us if you have any questions:  
Qi (Alex) Song: qisong@andrew.cmu.edu; sqsq3178@gmail.com  
Ziv Bar-Joseph: zivbj@andrew.cmu.edu

# Citation
Comming soon!

# Copyright
©2021 Qi Song, Ziv Bar-Joseph. [Systems Biology Group at Carnegie Mellon University](http://www.sb.cs.cmu.edu/). All rights reserved.

