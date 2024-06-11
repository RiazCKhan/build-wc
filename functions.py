def byte_count(filename):
    total_byte = 0
    with open(filename, "rb") as file:
        for line in file:
            total_byte += len(line)
    print("{} {}".format(total_byte, filename))


def line_count(filename):
    total_line = 0
    with open(filename, "r") as file:
        for line in file:
            total_line += line.count(line)
    print("{} {}".format(total_line, filename))


def word_count(filename):
    total_word = 0
    with open(filename, "r") as file:
        for line in file:
            string_arr = line.split()
            if len(string_arr) != 0:
                total_word += len(string_arr)
    print("{} {}".format(total_word, filename))


def char_count(filename):
    total_char = 0
    with open(filename, "r") as file:
        for line in file:
            string_arr = line.split()
            if len(string_arr) != 0:
                for string in string_arr:
                    total_char += string.count(string)
    print("{} {}".format(total_char, filename))
