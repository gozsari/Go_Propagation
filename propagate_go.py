def propagate_go(go_id, parent_set, go_term_dict):
    if len(go_term_dict[go_id]) == 0:
        return parent_set
    for parent in go_term_dict[go_id]:
        parent_set.add(parent)

    for parent in go_term_dict[go_id]:
        propagate_go(parent, parent_set, go_term_dict)
    return parent_set
def form_all_go_parents_dict(go_term_dict):
    go_parents_dict = dict()

    for go_id in go_term_dict:
        parent_set = set()
        parent_set = propagate_go(go_id, parent_set, go_term_dict)
        go_parents_dict[go_id] = parent_set

    return go_parents_dict
