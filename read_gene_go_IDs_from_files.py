import os
path = "input_folder"
def file_reader(input_file_name, seperator, geneColumn, goColumn):
    gene_goID_Dict = dict()
    if seperator=="commo":
        seperator = ","
    elif seperator== "tab":
        seperator = "\t"
    elif seperator == "space":
        seperator = " "
    with open("{}/{}".format(path, input_file_name), mode="r") as fp:
        for i, line in enumerate(fp):
            line_list = (line.strip().split(seperator))
            #First line is assumed to be identification line for each column
            if i > 0:
                gene_id = line_list[geneColumn].strip()
                if gene_id not in gene_goID_Dict:
                    gene_goID_Dict[gene_id] = set()
                go_id = line_list[goColumn].strip()
                gene_goID_Dict[gene_id].add(go_id)
    fp.close()
    return gene_goID_Dict


