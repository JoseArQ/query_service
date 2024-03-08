import argparse
from sort_number_blocks import sort_numbers_blocks

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Sort numbers in blocks.")
    parser.add_argument("numbers", metavar="N", type=int, nargs="+",
                        help="A list of numbers to be sorted in blocks.")
    args = parser.parse_args()

    result = sort_numbers_blocks(args.numbers)
    print(result)