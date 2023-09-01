# This script computes P(x0) andP'(x0) sing Horner's method
#
# Written by Jose Lis Paredes 08/31/2023

import numpy as np

def Horners_Method(polynomial, x0):
    # Check the interval is a list
    if not isinstance(polynomial, list):
        return print("The interval must be list of coefficients of the form [a_n a_n-1  ...  a_0]")

    elif not(all([isinstance(item, float) for item in polynomial])):
        return print("The polynomial coefficients must be floats")

    # Compute b_n for P(x)
    y = polynomial[0]

    # Compute b_n-1 for Q
    z = polynomial[0]

    print("{0:s}     {1:s}".format("a_n", "b_n"))
    print("{0:>4.1f}   {1:>4.1f}".format(polynomial[0],y))

    index = 0

    for coefficient in polynomial[1:-1]:

        # Compute b_j for P
        y = x0 * y + coefficient

        # Compute b_j-1 for Q
        z = x0 * z + y

        index += 1
        print("{0:>4.1f}   {1:>4.1f}".format(polynomial[index],y))


    # Compute b_0 for P
    y = x0 * y + polynomial[-1]
    print("{0:1.1f}   {1:1.1f}".format(polynomial[-1],y))


    print(f'\nP(x0) is {y}, and P\'(x0) is {z}')


if __name__ == '__main__':
    Horners_Method([2.0, 0.0, -3.0, 3.0, -4.0], -2)