import argparse

def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-item_name",
        type = str,
        help = "input item name",
    )

    parser.add_argument(
        "-item_description",
        type = str,
        help = "input item description",
    )

    parser.add_argument(
        "-contact_info",
        type = str,
        help = "input contacter information",
    )

    args = parser.parse_args()

    return args