
def read_goBasicObo():
    file_ = open("go-basic.obo", "r")
    go_term_dict= dict()
    go_id=""
    for line in file_:
        parts = line.split(": ")
        if parts[0] == "id":
            go_id = parts[1].strip()
            if go_id != "" and go_id not in go_term_dict:
                go_term_dict[go_id] = list()
        elif parts[0] == "is_a":
            parts_is_a = parts[1].split("!")
            go_term_dict[go_id].append(parts_is_a[0].strip())
        elif parts[0] == "relationship":
            parts_part_of = parts[1].split(" ")
            if parts_part_of[0] == "part_of":
                go_term_dict[go_id].append(parts_part_of[1].strip())
    return go_term_dict

