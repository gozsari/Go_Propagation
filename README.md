# Go_Propagation
 This repository is created to propogate go terms with respect to go hierarchy in go_basic.obo file

* The following figure shows a sample of Go term hierarchy
![alt text](https://github.com/gozsari/Go_Propagation/blob/master/images/sample_go.PNG)

## Installation

SLPred is a command-line prediction tool written in Python 3.7.1. SLPred was developed and tested in Ubuntu 20.04 LTS. Please make sure that you have **Anaconda** installed on  your computer and  run the below commands to install requirements. Dependencies are available in requirements.txt file.

```
conda create -n slpred_env python=3.7
conda activate slpred_env
pip install -r requirements.txt
```

## How to run SLPred to obtain the predictions 

## Preparation to run SLPred

* Clone the Git Repository
* In terminal or command line navigate into **SLPred** folder
* Then run the following commands

```
chmod +x download_extract_data.sh
./download_extract_data.sh
```

### Input file 

* The input file must be located under **input_files/fasta_files** folder.
* It must be in fasta format
* A sample is also given as **input_files/fasta_files/input.fasta**

### Explanation of Parameters

* **--file**: this is the file name of the fasta file. For example if fasta file name is **input.fasta**, this argument must be just **input**

### The command to run SLPred is as follows:
```
python run_SLPred.py --file input 
```
### Output file

* The results (predictions) will be located under **predictions** folder with the name: **input_predictions.csv**
* The prediction is indicated with 1 (positive) and 0 (negative) for the corresponding location in the output file

## License

SLPred
    Copyright (C) 2020 CanSyL

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

