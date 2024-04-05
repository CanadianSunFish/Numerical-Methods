import time
import numpy as np
import matplotlib.pyplot as plt
from typing import Optional, Union

"""
@author Jeremy Hopkins
@author Iris Yang
@version 0.1.3
"""
class Secant():

    def __init__(
        self, 
        f: callable, 
        a: Union[int, float], 
        b: Union[int, float],
        error: Optional[Union[int, float]] = None,
        string_func: Optional[str] = None,
        func_solution: Optional[float] = None
    ):
        """Construct `Secant`
        
            Args:
                f: Callable representation of function to be estimated>
                a: Min point value.
                b: Max point value
                error: Error bounds.
                string_func: String representation of function being estimated.

        """
        
        self.count = 0
        self.approx_vals = []
        self.solution = 0

        assert callable(f), "f must be callable"
        self.f = f

        assert isinstance(a, (int, float)), "a must be int or float"
        self.a = a

        assert isinstance(b, (int, float)), "b must be int or float"
        self.b = b

        if error is None:
            error = 0.01

        assert error >= 0.01, "secant error must be 0.01 or greater"

        assert isinstance(error, (int, float)), "error must be int or float type"
        self.error = error

        assert isinstance(string_func, str), "string_func must be string representation of function"
        self.string_func = string_func

        if func_solution is not None:
            assert isinstance(func_solution, float), "func_solution must be float"
        self.func_solution = func_solution


    def solve(self) -> float:

        if (self.f(self.a) * self.f(self.b) >= 0):
            raise Exception(f"root not in range [{self.a}, {self.b}]")

        self.count = 0
        self.approx_vals = []

        self.solution = self.method(self.f, self.a, self.b)
        return self.solution

        
    def method(self, f, a, b):

        self.count += 1

        x = a - (f(a) * ((b - a)/(f(a) - f(b))))
        # print(x)

        self.approx_vals.append(x)
        
        if (np.abs(f(x)) < self.error):
            return x

        if ((f(a) * f(x)) < 0):
            return self.method(f, a, x)

        if ((f(b) * f(x)) < 0):
            return self.method(f, x, b)


    def plot_solution(self) -> tuple[plt.Figure, plt.Axes]:
        fig, ax = plt.subplots()
        if self.string_func is not None:
            ax.set_title("Secant Method for " + self.string_func)
        else:
            ax.set_title("Secant Method")
        ax.set_xlabel("Number of Computations")
        ax.set_ylabel("Approximation")
        ax.text(0.96, 0.05, f'Solution: {self.solution:.5f}', ha='right', va='bottom', transform=ax.transAxes)
        ax.plot(range(len(self.approx_vals)), self.approx_vals, label='Approximation')
        ax.scatter(range(len(self.approx_vals)), self.approx_vals, s=5)
        if self.func_solution is not None:
            ax.axhline(y=self.solution, color='lightgreen', linestyle='-', label='Solution')
        ax.legend()
        
        return fig, ax