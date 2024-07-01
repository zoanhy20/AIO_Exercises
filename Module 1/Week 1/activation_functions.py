import math

alpha = 0.01


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def check_activation_function(activation):
    if activation != 'sigmoid' and activation != 'relu' and activation != 'elu':
        return False
    return True


def exercise2():
    x = input('Input x = ')

    if not is_number(x):
        return print('x must be a number')

    activation = input('Input activation function (sigmoid|relu|elu): ')

    if not check_activation_function(activation):
        return print(f'{activation} is not supported')

    x = float(x)

    if activation == 'sigmoid':
        result = 1 / (1 + math.e ** -x)
    elif activation == 'relu':
        result = x if x <= 0 else 0
    elif activation == 'elu':
        result = alpha * (math.e ** x - 1) if x <= 0 else x

    return print(f'{activation}: f({x}) = {result}')


if __name__ == '__main__':
    exercise2()
