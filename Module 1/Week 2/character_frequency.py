from pprint import pprint


def count_chars(string):

    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


pprint(count_chars('Happiness'))
