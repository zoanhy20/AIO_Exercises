import random
import math


def exercise3():
    num_samples = input(
        'Input number of samples (interger number) which are generated: ')

    if not num_samples.isnumeric():
        return print('number of samples must be an integer number')

    num_samples = int(num_samples)

    predict = []
    target = []

    for i in range(num_samples):
        predict.append(random.uniform(0.0, 10.0))
        target.append(random.uniform(0.0, 10.0))

    loss = input('Input loss name (MAE|MSE|RMSE): ')

    for i in range(num_samples):
        print(f'loss name: {loss}, sample: {i}, pred: {
              predict[i]}, target: {target[i]}')

    if loss == 'MAE':
        result = sum([abs(predict[i] - target[i])]
                     for i in range(num_samples)) / num_samples
    elif loss == 'MSE':
        result = sum([(predict[i] - target[i]) **
                     2 for i in range(num_samples)]) / num_samples
    elif loss == 'RMSE':
        result = math.sqrt(
            sum([(predict[i] - target[i]) ** 2 for i in range(num_samples)]) / num_samples)

    return print(f'final {loss}: {result}')


if __name__ == '__main__':
    exercise3()
