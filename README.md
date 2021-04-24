# Go_Propagation
 This repository is created to propagate go terms with respect to go hierarchy defined in **go_basic.obo** file by using **is_a** and **part_of** relations.
* The following figure shows a sample of Go term hierarchy
![alt text](https://github.com/gozsari/Go_Propagation/blob/main/images/sample_go.PNG)

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
python main.py --inputFile ProtBench_Benchmark2_EnsemblOrthology_Swiss-Prot_annotations_nonpropagated_20210211.txt --seperator tab --geneColumn 1 --goColumn 4

```
### Output file

* The results will be located under **output_folder** with the name: **input_file_name.csv**

## License

MIT License

Copyright (c) 2021 CanSyL

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

