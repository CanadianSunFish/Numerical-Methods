import time

from secant import *
from bisection import *
from false_position import *
from newton import *
from steffensen import *
from horner import *

"""
@author Jeremy Hopkins
@author Iris Yang
@version 0.2.1
"""
def secant_test(f, a, b, error, string_func, sol, txt_pos) -> None:
    start = time.time()
    secant = Secant(f, a, b, error, string_func, sol, txt_pos)
    solution = secant.solve()
    end = time.time()
    run = end - start

    print(" ")
    print("==============================")
    print("SECANT METHOD")
    print("Function: " + string_func)
    print(f"Solution: {solution}")
    print(f"Error: {np.abs(solution - sol)}")
    print(f"Iteration count: {secant.count}")
    print(f"Computation time: {run:.6f}s")
    print("==============================")
    print(" ")

    fig, ax = secant.plot_solution()
    plt.show()

def bisection_test(f, a, b, error, string_func, sol, txt_pos):
    start = time.time()
    bisection = Bisection(f, a, b, error, string_func, sol, txt_pos)
    solution = bisection.solve()
    end = time.time()
    run = end - start

    print(" ")
    print("==============================")
    print("BISECTION METHOD")
    print("Function: " + string_func)
    print(f"Solution: {solution}")
    print(f"Error: {np.abs(solution - sol)}")
    print(f"Iteration count: {bisection.count}")
    print(f"Computation time: {run:.6f}s")
    print("==============================")
    print(" ")

    fig, ax = bisection.plot_solution()
    plt.show()

def false_position_test(f, a, b, error, string_func, sol, txt_pos):
    start = time.time()
    false_position = FalsePosition(f, a, b, error, string_func, sol, txt_pos)
    solution = false_position.solve()
    end = time.time()
    run = end - start

    print(" ")
    print("==============================")
    print("FALSE POSITION METHOD")
    print("Function: " + string_func)
    print(f"Solution: {solution}")
    print(f"Error: {np.abs(solution - sol)}")
    print(f"Iteration count: {false_position.count}")
    print(f"Computation time: {run:.6f}s")
    print("==============================")
    print(" ")

    fig, ax = false_position.plot_solution()
    plt.show()

def newton_test(f, x, error, string_func, sol, txt_pos):
    start = time.time()
    newton = Newton(f, x, error, string_func, sol, txt_pos)
    solution = newton.solve()
    end = time.time()
    run = end - start

    print(" ")
    print("==============================")
    print("NEWTON METHOD")
    print("Function: " + string_func)
    print(f"Solution: {solution}")
    print(f"Error: {np.abs(solution - sol)}")
    print(f"Iteration count: {newton.count}")
    print(f"Computation time: {run:.6f}s")
    print("==============================")
    print(" ")

    fig, ax = newton.plot_solution()
    plt.show()

def steffensen_test(f, x, error, string_func, sol, txt_pos):
    start = time.time()
    steffensen = Steffensen(f, x, error, string_func, sol, txt_pos)
    solution = steffensen.solve()
    end = time.time()
    run = end - start

    print(" ")
    print("==============================")
    print("STEFFENSEN METHOD")
    print("Function: " + string_func)
    print(f"Solution: {solution}")
    print(f"Error: {np.abs(solution - sol)}")
    print(f"Iteration count: {steffensen.count}")
    print(f"Computation time: {run:.6f}s")
    print("==============================")
    print(" ")

    fig, ax = steffensen.plot_solution()
    plt.show()

def horner_test(polynomial, a, b, error, step, string_func):
    start = time.time()
    horner = Horner(polynomial, len(polynomial), a, b, error, step, string_func)
    x, y = horner.solve()
    end = time.time()
    run = end - start
    
    sol_arr = []
    for i in range(len(y)):
        y_sol = y[i]
        if (y_sol > -error and y_sol < error):
            x_sol = x[i]
            sol_arr.append(x_sol)

    print(" ")
    print("==============================")
    print("HORNER METHOD")
    print("Function: " + string_func)
    print(f"Solutions: {np.round(sol_arr[0], 2)}, {np.round(sol_arr[1], 2)}, {np.round(sol_arr[2], 2)}, {np.round(sol_arr[3], 2)}")
    print(f"Computation time: {run:.6f}s")
    print("==============================")
    print(" ")

    fig, ax = horner.plot_solution(x, y)
    plt.show()

def newton_error_test(f, x, error, string_func):
    start = time.time()
    newton = Newton(f, x, error, string_func, np.sqrt(2))
    start = newton._find_starting_error(0.001)
    end = time.time()
    run = end - start
    newton_val = Newton(f, start, 0.001)
    sol = newton_val.solve()
    
    print(" ")
    print("==============================")
    print("NEWTON 3 ITERATIONS TO 0.001 ERROR")
    print("Function: " + string_func)
    print(f"Starting Value: {start}")
    print(f"Number of Iterations Starting at {start}: {newton_val.count}")
    print(f"Solution Starting at {start}: {sol}")
    print(f"Computation time: {run:.6f}s")
    print("==============================")
    print(" ")

    fig, ax = newton.plot_solution()
    plt.show()

if __name__ == "__main__":

    f = lambda x: x**2 - 2
    
    secant_test(f, 0, 2, 0.01, "x\u00b2-2", np.sqrt(2), 'top left') # top left
    bisection_test(f, 0, 2, 1e-15, "x\u00b2-2", np.sqrt(2), 'bottom right') # fine
    false_position_test(f, 0, 2, 1e-15, "x\u00b2-2", np.sqrt(2), 'bottom left') # up a little or bottom left
    newton_test(f, 1, 1e-15, "x\u00b2-2", np.sqrt(2), 'bottom right') # fine
    steffensen_test(f, 1, 1e-15, "x\u00b2-2", np.sqrt(2), 'bottom right') # fine

    f = lambda x: x**3 - 0
    
    secant_test(f, -0.05, 0.05, 0.01, "x\u00b2-0", 0.0, 'bottom right') # fine
    bisection_test(f, -0.5, 0.5, 1e-3, "x\u00b2-0", 0.0, 'bottom right') # fine
    false_position_test(f, -0.5, 0.5, 1e-3, "x\u00b2-0", 0.0, 'bottom right') # fine
    newton_test(f, 0.5, 1e-3, "x\u00b2-0", 0.0, 'bottom left') # bottom left
    steffensen_test(f, 0.5, 1e-3, "x\u00b2-0", 0.0, 'bottom left') # bottom left

    f = lambda x: x**2 - 3
    
    secant_test(f, 1, 2, 0.01, r"$x^2-3$", np.sqrt(3), 'bottom right') # fine
    bisection_test(f, 1, 2, 1e-5, r"$x^2-3$", np.sqrt(3), 'bottom right') # fine
    false_position_test(f, 1, 2, 1e-5, r"$x^2-3$", np.sqrt(3), 'bottom left') # fine
    newton_test(f, 2, 1e-5, r"$x^2-3$", np.sqrt(3), 'bottom right') # bottom left
    steffensen_test(f, 2, 1e-5, r"$x^2-3$", np.sqrt(3), 'bottom right') # bottom left

    polynomial = [8, 0, -8, 0, 1]
    horner_test(polynomial, -1.1, 1.1, 0.002, 0.001, r"$8x^4-8x^2-1$")

    polynomial = [1, 0, -6/7, 0, 3/35]
    horner_test(polynomial, -1.1, 1.1, 0.002, 0.01, r"$x^4-\frac{6}{7}x^2-\frac{3}{35}$")

    f = lambda x: x**2 - 2

    newton_error_test(f, 1, 1e-15, r"$x^2-2$")
