def byte_count():
    total_byte = 0
    with open(args.byte, "rb") as file:
        for line in file:
            total_byte += len(line)
    print("{} {}".format(total_byte, args.byte))


def line_count():
    total_line = 0
    with open(args.line, "r") as file:
        for line in file:
            total_line += line.count(line)
    print("{} {}".format(total_line, args.line))


def word_count():
    total_word = 0
    with open(args.word, "r") as file:
        for line in file:
            string_arr = line.split()
            if len(string_arr) != 0:
                total_word += len(string_arr)
    print("{} {}".format(total_word, args.word))


def char_count():
    total_char = 0
    with open(args.char, "r") as file:
        for line in file:
            string_arr = line.split()
            if len(string_arr) != 0:
                for string in string_arr:
                    total_char += string.count(string)
    print("{} {}".format(total_char, args.char))
