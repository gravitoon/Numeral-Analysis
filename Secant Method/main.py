# This script uses the secant method to calculate the root of a given function
# given two initial points
#
# p_n = p_n-1 - f(p_n-1)( p_n-1 - p_n-2) / (f(p_n-1) - f(p_n-2))
#
# Written by Jose Luis Paredes 07/12/2023

import numpy as np

def func(x):
    return np.cos(x) - x

def secant_method(initial_approx, tolerance = 0.001, max_iter = 20):
    # Check the remaining inputs to the function
    if type(tolerance) != float:
        return print(f'The initial tolerance must be a floating point number')

    elif type(max_iter) != int:
        return print(f'The max_iter nust be an integer')

    if not isinstance(initial_approx, list):
        return print("The interval must be list of the form [a b]")

    elif len(initial_approx) != 2:
        return print("The interval must be list of the form [a b]")

    elif not (all([isinstance(item, float) for item in initial_approx])):
        return print("The interval must be list of floating point numbers")

    # Defined initial values
    iter = 2
    p_0 = initial_approx[0]
    p_1 = initial_approx[1]
    q_0 = func(p_0)
    q_1 = func(p_1)

    print("{0:<2s} {1:^16s} ".format("n","p_n",))

    while max_iter >= iter:
        if (q_1 - q_0) == 0:
            print(f'The points q_1 and q_0 are equal')
            break

        p_n = p_1 - (q_1*(p_1- p_0))/(q_1 - q_0)
        print("{0:<3d}   {1:^.9f}".format(iter, p_0))

        if np.abs(p_n - p_1) < tolerance:
            print(f'\n For the initial p_0 = {initial_approx} the root is {p_n}')
            print(f'\n The error of the approximation is {np.abs(p_n - p_0) /np.abs(p_n)}')
            break

        iter += 1

        # Use the previos point to set up the next secant
        p_0 = p_1
        q_0 = q_1
        p_1 = p_n
        q_1 = func(p_n)

    if iter > max_iter:
        print(f"No root was found within the given tolerance after {iter} iterations")

if __name__ == '__main__':
    secant_method([0.5, np.pi/4], 0.00001, 15)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

