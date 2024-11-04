import os
import parse_args

def find_item(args):
    input_path = f"{os.path.abspath(os.getcwd(), os.pardir)}/item_files"
    f = open(os.path.join(input_path, "items.txt"), "w")
    item_list = f.readlines()
    items = list()
    for item in item_list:
        items.append(list(item.strip("\n")))
    for item in items:
        item_suffix1 = item.split(":",1)[-1]
        item_name, item_suffix2 = item_suffix1.split(",",1)
        item_suffix3 = item_suffix2.split(":",1)[-1]
        item_desc, item_suffix4 = item_suffix3.split(",",1)
        cont_info = item_suffix4.split(":",1)[-1]
        if args.item_name == item_name:
            print("Item found:" + "\n")
            print("item_name: " + item_name + "\n")
            print("item_description: " + item_desc + "\n")
            print("contact_info: " + cont_info + "\n")
            break
        raise NotImplementedError(f"Item not found")

    return


if __name__ == "__main__":
    args = parse_args()
    find_item(args)