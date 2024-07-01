num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3

for i in range(len(num_list) - k + 1):
    sub_lst = num_list[i: i + k]

    row = num_list.copy()
    row[i] = f'[{num_list[i]}'
    row[i + k - 1] = f'{num_list[i + k - 1]}]'

    output = ', '.join([str(v) for v in row]) + f' => max {max(sub_lst)}'

    print(output)
