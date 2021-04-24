# Go_Propagation
 This repository is created to propogate go terms with respect to go hierarchy in go_basic.obo file

* The following figure shows a sample of Go term hierarchy
![alt text](https://github.com/gozsari/Go_Propagation/images/sample_go.PNG)

## Installation



## How to run Go_Propagation to obtain the propogation results 

## Preparation to run Go_Propagation

* Clone the Git Repository

### Input file 

* The input file must be located under **input_folder.
* It must be in either a txt or cvs format
* The colums of input file muust be seperated with either space, tab or commo.
* First line of input file is assumed to be identification line for each column
### Explanation of Parameters
* **--inputFile**: protein and go_terms input_file_name, input file name should be written with extension such as **.txt, .csv**
* **--seperator**: seperator of input file columns, default it is **space**, other options can be **tab** or **commo**'  
* **--geneColumn**: gene/protein column number(integer) in the input file, starting index = 0
* **--goColumn**: go term column number(integer) in the input file, starting index = 0
### A sample command to run Go_Propagation is as follows:
```
main.py --inputFile ProtBench_Benchmark2_EnsemblOrthology_Swiss-Prot_annotations_nonpropagated_20210211.txt --seperator tab --geneColumn 1 --goColumn 4

```
### Output file

* The results will be located under **output_folder** with the name: **input_file_name.csv**

## License

Go_Propagation
    Copyright (C) 2020 CanSyL

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

