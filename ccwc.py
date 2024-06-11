import argparse
from functions import byte_count, line_count, word_count, char_count

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
parser.add_argument(
    "-w",
    "--word",
    help="The number of words in each input file is written to the standard output.",
)
parser.add_argument(
    "-m",
    "--char",
    help="The number of characters in each input file is written to the standard output.",
)
args = parser.parse_args()

if args.byte:
    byte_count()
elif args.line:
    line_count()
elif args.word:
    word_count()
elif args.char:
    char_count()
