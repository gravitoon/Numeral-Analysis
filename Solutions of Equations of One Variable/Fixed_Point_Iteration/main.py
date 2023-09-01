# The number p is a fixed point iteration for a given function g if p = g(p). This script
# finds a solution to p = g(p) given an initial approximation p0
#
# To approximate the fixed point of a function g, we choose an initial approximation p_0
# and generate the sequence p_n (n = 0 to infinity) by letting p_n = g(p_n-1) for each n>=1.
# If the sequence converges to p and g is continuous then
#
# p = lim p_n (n-> inf) = lim g( p_n-1 ) (n->inf) = g (lim p_n n->inf) = g(p)
#
# Written by Jose Lis Paredes 06/17/2023

import numpy as np

def func(x):
    return (1/2)*(10 - x**3)**(1/2)

def fixed_point_iteration(init_approx, tolerance=0.000000001, max_iter = 40):

    # Check the input to the function
    if type(init_approx) != float:
        return print(f'The initial approximation nust be a number')

    elif type(tolerance) != float:
        return print(f'The initial tolerance nust be a number')

    elif type(max_iter) != int:
        return print(f'The max_iter nust be an integer')

    # Initialize some parameters
    iter = 1
    p_0 = init_approx

    print("{0:<3s}   {1:^16s}".format("n  ","p"))

    # Check while the number of iterations is less than the max
    while iter < max_iter:
        # Compute p_i
        p_i = func(p_0)

        print("{0:<3d}   {1:^.9f}".format(iter, p_0))

        if np.abs(p_i - p_0) < tolerance:
            print(f'\n For the initial p0 = {init_approx} the root is {p_i}')
            break

        # Next iteration
        iter += 1

        # Update p
        p_0 = p_i

    if iter > max_iter:
        print(f'Maximum number of iteration reached. p is outside the given tolerance')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fixed_point_iteration(1.5)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
