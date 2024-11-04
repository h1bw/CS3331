import os
import parse_args

def add_item(args):

    output_path = f"{os.path.abspath(os.getcwd(), os.pardir)}/item_files"
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    with open(os.path.join(output_path, "items.txt"), "w") as f:
        f.write("item_name:" + args.item_name + ",")
        f.write("item_description:" + args.item_description + ",")
        f.write("contact_info:" + args.contact_info + "\n")

    return

if __name__ == "__main__":
    args = parse_args()
    add_item(args)