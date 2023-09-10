# This script uses Muller's method to find the root (real or complex)
# of a polynomial given three initial approximations
#
# p_n = p_n-1 - 2c / (b + sgn(b) sqrt(b^2 - 4ac))
#
# with
# c = f(p_n-1)
# b = (p_n-3 - p_n-1)^2 (f(p_n-2) - f(p_n-1)) - (p_n-2 - p_n-1)^2(f(p_n-3) - f(p_n-1)) /
#                                          ((p_n-3 - p_n-1)(p_n-2 - p_n-1)(p_n-3 - p_n-2))
# c = (p_n-2 - p_n-1)^2 (f(p_n-3) - f(p_n-1)) - (p_n-3 - p_n-1)(f(p_n-2) - f(p_n-1)) /
#                                          ((p_n-3 - p_n-1)(p_n-2 - p_n-1)(p_n-3 - p_n-2))

#
# Written by Jose Luis Paredes 09/09/2023

import cmath as cm

def func(x):
    return x**4 - 3*x**3 + x**2 + x + 1

def muller_method(initial_approx, tolerance = 0.001, max_iter = 20):
    # Check the remaining inputs to the function
    if type(tolerance) != float:
        return print(f'The initial tolerance must be a floating point number')

    elif type(max_iter) != int:
        return print(f'The max_iter nust be an integer')

    if not isinstance(initial_approx, list):
        return print("The interval must be list of the form [p0, p1, p2]")

    elif len(initial_approx) != 3:
        return print("The interval must be list of the form [p0, p1, p2]")

    elif not (all([isinstance(item, float) for item in initial_approx])):
        return print("The interval must be list of floating point numbers")

    # Defined initial values
    iteration = 3
    p_0 = initial_approx[0]
    p_1 = initial_approx[1]
    p_2 = initial_approx[2]

    print("{0:<2s} {1:^20s} {2:^20s}".format("n","p_i", "f(p_i)"))

    while max_iter >= iteration:
        h_0 = p_0 - p_1
        h_1 = p_1 - p_2
        h_2 = p_0 - p_2

        if h_0 == 0:
            print(f'The points p_0 and p_1 are equal')
            break
        elif h_1 == 0:
            print(f'The points p_1 and p_2 are equal')
            break
        elif h_2 == 0:
            print(f'The points p_0 and p_2 are equal')
            break

        c = func(p_2)
        b = ((h_2 ** 2 * (func(p_1) - func(p_2))) - (h_1 ** 2 * (func(p_0) - func(p_2)))) / (h_0 * h_1 * h_2)
        a = ((h_1 * (func(p_0) - func(p_2))) - (h_2 * (func(p_1) - func(p_2)))) / (h_0 * h_1 * h_2)
        disc = cm.sqrt(b**2 - 4*a*c)

        if abs(b - disc) < abs(b + disc):
            denominator = b + disc

        else:
            denominator = b - disc

        h = -2 * c / denominator
        p = p_2 + h

        if abs(h) < tolerance:
            print(f'\n\nThe root is {p}')
            return

        print("{0:<2d} {1:^20f} {2:^20f}".format(iteration, p, func(p)))

        p_0 = p_1
        p_1 = p_2
        p_2 = p
        iteration += 1

    if iteration > max_iter:
        print(f"No root was found within the given tolerance after {iteration} iterations")

if __name__ == '__main__':
    muller_method([0.5, -0.5, 0.0], 0.00001, 20)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

