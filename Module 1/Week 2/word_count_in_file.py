from pprint import pprint

file_path = 'Module 1/Week 2/P1_data.txt'


def word_count(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


pprint(word_count(file_path))
