# By applying a modification of Aitkens Delta square method to a linearly convergent sequence
# obtained from fixed point iteration, we can accelerate the convergence to quadratic.
# p_0, p_1 = g(p_0), p_2 = g(p_1)
#
#                   p_n = p_n -  (p_n+1 - pn)^2 / (p_n+2 - 2 p_n+1 + p_n)
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



def func(x):
    return (10/(x+4))**(1/2)

def steffensen_method(initial_approx, tolerance = 0.001, max_iter = 20):
    # Check the remaining inputs to the function
    if type(tolerance) != float:
        return print(f'The initial tolerance must be a floating point number')

    elif type(max_iter) != int:
        return print(f'The max_iter nust be an integer')

    elif type(initial_approx) != float:
        return print(f'The initial approximation must be a floating point number')

    # Defined initial values
    iteration = 1
    p_0 = initial_approx

    while iteration < max_iter:
        p_1 = func(p_0)
        p_2 = func(p_1)
        p = p_0 - (p_1 - p_0)**2/(p_2 - 2*p_1 + p_0)

        print("{0:<3d} {1:^.9f} {1:^.9f} {1:^.9f}".format(iteration, p_0, p_1, p_2))

        if abs(p - p_0) < tolerance:
            print(f'\nFor the initial p_0 = {initial_approx} the root is {p}')
            break

        iteration += 1
        # Update p_0
        p_0 = p

    if iteration > max_iter:
        print(f"No root was found within the given tolerance after {iter} iterations")

if __name__ == '__main__':
    steffensen_method(1.5, 0.00001, 15)