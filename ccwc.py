import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-c",
    "--byte",
    help="The number of bytes in each input file is written to the standard output.",
)
parser.add_argument(
    "-l",
    "--line",
    help="The number of lines in each input file is written to the standard output.",
)
args = parser.parse_args()

if args.byte:
    total_byte = 0
    with open(args.byte, "rb") as file:
        for line in file:
            total_byte += len(line)
    print("{} {}".format(total_byte, args.byte))
elif args.line:
    total_line = 0
    with open(args.line, "r") as file:
        for line in file:
            total_line += line.count(line)
    print("{} {}".format(total_line, args.line))