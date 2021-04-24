from propagate_go import form_all_go_parents_dict
from read_go_basic_obo import read_goBasicObo
from read_gene_go_IDs_from_files import file_reader
from write_to_file import write_to_file
import argparse

parser = argparse.ArgumentParser(description='Go_Propagation arguments')
parser.add_argument(
    '--inputFile',
    type=str,
    default="input",
    help='protein and go_terms input_file_name, input file name should be written with extension such as .txt, .csv')
parser.add_argument(
    '--seperator',
    type=str,
    default="space",
    help='seperator of input file columns, default it is space, other options can be tab or commo')
parser.add_argument(
    '--geneColumn',
    type=int,
    default=0,
    help='gene/protein column number in the input file, starting index = 0')
parser.add_argument(
    '--goColumn',
    type=int,
    default=1,
    help='go term column number in the input file, starting index = 0')

if __name__ == "__main__":
    args = parser.parse_args()
    input_file_name = args.inputFile
    seperator = args.seperator

    geneColumn = args.geneColumn
    goColumn = args.goColumn
    gene_goID_Dict = file_reader(input_file_name, seperator, geneColumn, goColumn)
    go_term_dict = read_goBasicObo()
    go_parents_dict = form_all_go_parents_dict(go_term_dict)

    all_gene_goIDs_propagated = dict()
    for gene_id in gene_goID_Dict:
        go_list = set()
        for go_id in gene_goID_Dict[gene_id]:
            go_list.add(go_id)
            for parent_goID in go_parents_dict[go_id]:
                go_list.add(parent_goID)
        all_gene_goIDs_propagated[gene_id] = go_list

    write_to_file(input_file_name, all_gene_goIDs_propagated)

