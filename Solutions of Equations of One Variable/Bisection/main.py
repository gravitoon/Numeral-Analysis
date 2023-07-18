# This script uses the bisection method to calculate the root of a function on a given interval [a,b] with a given
# tolerance and a given number of iterations.
#
# Suppose f is a continuous function on the interval [a, b] with f(a) and f(b) of opposite sign. Set a1 = a and b1 = b
# and let p1 be the midpoint of [a, b];
# Set p1 = a1 + (b1 - a1)/2
# If f(p1) = 0 then p = p1
# If f(p1) !=0 then f(p1) has the same sign of either f(a1) or f(b1)
#    - If f(p1) and f(a1) have the same sign, p belongs in (p1, b1). Set a2 = p1 and b2 = b1
#    - If f(p1) and f(a1) have opposite sign, p belongs in (a1, p1). Set a2 = a1 and b2 = p1
# Reapply the process on the interval (a2, b2)
#
# Written by Jose Lis Paredes 06/08/2023

import numpy as np

def func(x):
    return x**3 + 4*x**2 - 10

def bisection(interval, tolerance = 0.001, max_iter = 20):
    # Check the interval is a list
    if not isinstance(interval, list):
        return print("The interval must be list of the form [a b]")

    elif len(interval) != 2:
        return print("The interval must be list of the form [a b]")

    elif not(all([isinstance(item, float) for item in interval])):
        return print("The interval must be list of numbers")

    # Check the remaining inputs to the function
    if type(tolerance) != float:
        return print(f'The initial tolerance nust be a number')

    elif type(max_iter) != int:
        return print(f'The max_iter nust be an integer')


    # Calculate the value of the function at both interval endpoints
    f_a = func(interval[0])
    f_b = func(interval[1])

    # For the bisection method to work we require the sign of the function
    # to be distinct
    if np.sign(f_a) == 0:
        print(f"{interval[0]} is a root of the function")
        return

    elif np.sign(f_b) == 0:
        print(f"{interval[1]} is a root of the equation")
        return

    elif np.sign(f_a) == np.sign(f_b):
        print(f"The sign of f({interval[0]} and f({interval[1]} is the same")
        print("Choose a different interval")

    #Initialize the iterations
    iter = 1
    lower_bound = interval[0]
    upper_bound = interval[1]
    root = lower_bound + (upper_bound - lower_bound)/2

    print("{0:<3s}   {1:^16s} {2:^12s}   {3:^12s}    {4:^12s}".format("  n","a_n","b_n", "p_n", "f(p_n)"))

    while max_iter >= iter:
        len_interval = (upper_bound - lower_bound)/2
        mid_pt = lower_bound + len_interval
        f_mid_pt = func(mid_pt)

        if (f_mid_pt == 0) or (len_interval < tolerance):
            error = abs(upper_bound - root)
            print(f"\n\n The root is {root} within an error of {error}")
            return

        print("{0:>3d}    {1:<.10f}   {2:<.10f}    {3:<.10f}    {4:<.10f}".format(iter, lower_bound, upper_bound, mid_pt, f_mid_pt))

        iter += 1

        if np.sign(f_a * f_mid_pt) > 0:
            lower_bound = mid_pt
            f_a = f_mid_pt

        else:
            upper_bound = mid_pt
            f_b = f_mid_pt

        root = mid_pt

    print(f"No root was found within the given tolerance after {iter} iterations")

if __name__ == '__main__':
    bisection([1.0, 2.0], 0.0001, 15)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
