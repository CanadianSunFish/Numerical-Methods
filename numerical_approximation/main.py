import time

from secant import *
from bisection import *
from false_position import *
from newton import *
from steffensen import *

def secant_test(f, a, b, error, string_func, sol) -> None:
    start = time.time()
    secant = Secant(f, a, b, error, string_func, sol)
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
    print(f"Computation time: {run:.8f}s")
    print("==============================")
    print(" ")

    fig, ax = secant.plot_solution()
    plt.show()


def bisection_test(f, a, b, error, string_func, sol):
    start = time.time()
    bisection = Bisection(f, a, b, error, string_func, sol)
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
    print(f"Computation time: {run:.8f}s")
    print("==============================")
    print(" ")

    fig, ax = bisection.plot_solution()
    plt.show()

def false_position_test(f, a, b, error, string_func, sol):
    start = time.time()
    false_position = FalsePosition(f, a, b, error, string_func, sol)
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
    print(f"Computation time: {run:.8f}s")
    print("==============================")
    print(" ")

    fig, ax = false_position.plot_solution()
    plt.show()


def newton_test(f, x, error, string_func, sol):
    start = time.time()
    newton = Newton(f, x, error, string_func, sol)
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
    print(f"Computation time: {run:.8f}s")
    print("==============================")
    print(" ")

    fig, ax = newton.plot_solution()
    plt.show()


def steffensen_test(f, x, error, string_func, sol):
    start = time.time()
    steffensen = Steffensen(f, x, error, string_func, sol)
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
    print(f"Computation time: {run:.8f}s")
    print("==============================")
    print(" ")

    fig, ax = steffensen.plot_solution()
    plt.show()

if __name__ == "__main__":

    f = lambda x: x**2 - 2
    
    secant_test(f, 0, 2, 0.1, "x\u00b2-1", np.sqrt(2))
    bisection_test(f, 0, 2, 1e-15, "x\u00b2-1", np.sqrt(2))
    false_position_test(f, 0, 2, 1e-15, "x\u00b2-1", np.sqrt(2))
    newton_test(f, 1, 1e-15, "x\u00b2-1", np.sqrt(2))
    steffensen_test(f, 1, 1e-15, "x\u00b2-1", np.sqrt(2))

    f = lambda x: x**3 - 0
    
    secant_test(f, -0.05, 0.05, 0.01, "x\u00b2-0", 0.0)
    bisection_test(f, -0.5, 0.5, 1e-3, "x\u00b2-0", 0.0)
    false_position_test(f, -0.5, 0.5, 1e-3, "x\u00b2-0", 0.0)
    newton_test(f, 0.5, 1e-3, "x\u00b2-0", 0.0)
    steffensen_test(f, 0.5, 1e-3, "x\u00b2-0", 0.0)

    
