import argparse
from functions import byte_count, line_count, word_count, char_count, byte_line_word_count

parser = argparse.ArgumentParser()
parser.add_argument(
    "filename",
    help="The number of bytes, lines, and words from input file.",
)
parser.add_argument(
    "-c",
    help="The number of bytes in each input file is written to the standard output.",
    action="store_true",
)
parser.add_argument(
    "-l",
    help="The number of lines in each input file is written to the standard output.",
    action="store_true",
)
parser.add_argument(
    "-w",
    "-word",
    help="The number of words in each input file is written to the standard output.",
    action="store_true",
)
parser.add_argument(
    "-m",
    "-char",
    help="The number of characters in each input file is written to the standard output.",
    action="store_true",
)
args = parser.parse_args()


if args.c:
    byte_count(args.filename)
elif args.l:
    line_count(args.filename)
elif args.w:
    word_count(args.filename)
elif args.m:
    char_count(args.filename)
elif args.filename:
    byte_line_word_count(args.filename)
