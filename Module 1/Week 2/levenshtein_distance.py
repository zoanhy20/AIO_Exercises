from pprint import pprint

source = 'yu'
target = 'you'


def levenshtein_distance(source, target):
    rows = len(source) + 1
    cols = len(target) + 1

    D = [[0] * cols for _ in range(rows)]

    for i in range(cols):
        D[0][i] = i

    for i in range(rows):
        D[i][0] = i

    for i in range(1, rows):
        for j in range(1, cols):
            cost = 0 if source[i-1] == target[j-1] else 1

            D[i][j] = min(D[i-1][j] + 1,
                          D[i][j-1] + 1,
                          D[i-1][j-1] + cost)

    pprint(D)
    return D[rows - 1][cols - 1]


levenshtein_distance(source, target)
