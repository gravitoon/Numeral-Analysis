# This script uses the newton-raphson method to calculate the root of a given function
# given an initial approximation initial_approx
#
# Suppose that is a twice differentiable on [a,b] and that |p_n - p_0 | is small then
#
# p_n = p_n-1 = p_0 - f(p_0) / f'(p_0)
#
# Written by Jose Luis Paredes 06/22/2023

import numpy as np

def func(x):
    return np.cos(x) - x

def func_prime(x):
    return -np.sin(x) - 1

def newton_raphson(initial_approx, tolerance = 0.001, max_iter = 20):
    # Check the remaining inputs to the function
    if type(tolerance) != float:
        return print(f'The initial tolerance nust be a number')

    elif type(max_iter) != int:
        return print(f'The max_iter nust be an integer')

    elif type(initial_approx) != float:
        return print(f'The initial approximation nust be a float')

    iter = 1
    p_0 = initial_approx

    print("{0:<2s} {1:^16s} ".format("n","p_n",))

    while max_iter >= iter:

        if func_prime(p_0) == 0:
            print(f'The derivative at this point {p_0} is zero')
            break

        p_n = p_0 - func(p_0)/func_prime(p_0)
        print("{0:<3d}   {1:^.9f}".format(iter, p_0))

        if np.abs(p_n - p_0) < tolerance:
            print(f'\n For the initial p_0 = {initial_approx} the root is {p_n}')
            print(f'\n The error of the approximation is {np.abs(p_n - p_0) /np.abs(p_n)}')
            break

        iter += 1

        p_0 = p_n

    if iter > max_iter:
        print(f"No root was found within the given tolerance after {iter} iterations")

if __name__ == '__main__':
    newton_raphson(np.pi/4, 0.0001, 15)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
