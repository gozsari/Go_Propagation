def write_to_file(file_name, all_gene_goIDs_propagated):
    file_name_ = file_name.split('.')[0]
    with open("{}/{}_propagated_genes_goIDs.csv".format("output_folder", file_name_), "w") as fw:
        fw.write("GENE_ID, GO_TERM_ID\n")
        for gene_id in all_gene_goIDs_propagated:
            for go_id in all_gene_goIDs_propagated[gene_id]:
                fw.write("{}, {}\n".format(gene_id, go_id))
    fw.close()