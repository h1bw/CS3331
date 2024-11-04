import os
import parse_args

def delete_item(args):
    input_path = f"{os.path.abspath(os.getcwd(), os.pardir)}/item_files"
    f = open(os.path.join(input_path, "items.txt"), "w")
    item_list = f.readlines()
    items = list()
    for item in item_list:
        items.append(list(item.strip("\n")))
    for i, item in enumerate(items):
        item_suffix1 = item.split(":",1)[-1]
        item_name, item_suffix2 = item_suffix1.split(",",1)
        item_suffix3 = item_suffix2.split(":",1)[-1]
        item_desc, item_suffix4 = item_suffix3.split(",",1)
        cont_info = item_suffix4.split(":",1)[-1]
        if args.item_name == item_name and args.item_description == item_desc and args.contact_info == cont_info:
            del items[i]
            break
        raise NotImplementedError("Item not found")
    os.remove(os.path.join(input_path, "items.txt"))
    with open(os.path.join(input_path, "items.txt"), "w") as f:
        for item in items:
            f.write(item + "\n")
    return


if __name__ == "__main__":
    args = parse_args()
    delete_item(args)