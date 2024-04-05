import numpy as np
import matplotlib.pyplot as plt
from typing import Optional, Union

"""
@author Jeremy Hopkins
@author Iris Yang
@version 0.2.2
"""
class Bisection():

    def __init__(
        self, 
        f: callable, 
        a: Union[int, float], 
        b: Union[int, float],
        error: Optional[Union[int, float]] = None,
        string_func: Optional[str] = None,
        func_solution: Optional[float] = None,
        txt_pos: Optional[str] = 'bottom right'
    ):
        """Construct `Bisection`
        
            Args:
                f: Callable representation of function to be estimated>
                a: Min point value.
                b: Max point value
                error: Error bounds.
                string_func: String representation of function being estimated.
                func_sol: The true soltion to the function.
                txt_pos: Positioning for txt plotting.

        """
        self.error = error
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

        assert isinstance(error, (int, float)), "error must be int or float type"
        self.error = error

        if string_func is not None:
            assert isinstance(string_func, str), "string_func must be string representation of function"
        self.string_func = string_func

        if func_solution is not None:
            assert isinstance(func_solution, float), "func_solution must be float"
        self.func_solution = func_solution

        assert isinstance(txt_pos, str), "txt_pos must be a string"
        self.txt_pos = txt_pos


    def solve(self) -> float:

        self.count = 0
        self.approx_vals = []

        self.solution = self.method(self.f, self.a, self.b)

        return self.solution

        
    def method(self, f, a, b):

        self.count += 1

        if np.sign(f(a)) == np.sign(f(b)):
            raise Exception(
            "The scalars a and b do not bound a root")

        m = (a + b)/2
        self.approx_vals.append(m)

        if np.abs(f(m)) < self.error:
            return m
        elif np.sign(f(m)) == np.sign(f(a)):
            return self.method(f, m, b)
        elif np.sign(f(m)) == np.sign(f(b)):
            return self.method(f, a, m)


    def plot_solution(self) -> tuple[plt.Figure, plt.Axes]:
        fig, ax = plt.subplots()
        fig.set_size_inches(11, 8.5)
        if self.string_func is not None:
            ax.set_title("Bisection Method for " + self.string_func)
        else:
            ax.set_title("Bisection Method")
        ax.set_xlabel("Number of Computations")
        ax.set_ylabel("Approximation")
        if self.txt_pos == 'bottom right':
            ax.text(0.9675, 0.065, f'Target Solution: {self.func_solution:.1f}', ha='right', va='bottom', transform=ax.transAxes)
        if self.txt_pos == 'bottom left':
            ax.text(0.25, 0.065, f'Target Solution: {self.func_solution:.1f}', ha='right', va='bottom', transform=ax.transAxes)
        if self.txt_pos == 'top left':
            ax.text(0.25, 0.935, f'Target Solution: {self.func_solution:.1f}', ha='right', va='bottom', transform=ax.transAxes)
        if self.txt_pos == 'top right':
            ax.text(0.9675, 0.935, f'Target Solution: {self.func_solution:.1f}', ha='right', va='bottom', transform=ax.transAxes)
        ax.plot(range(len(self.approx_vals)), self.approx_vals, label='Approximation')
        ax.scatter(range(len(self.approx_vals)), self.approx_vals, s=5)
        if self.func_solution is not None:
            ax.axhline(y=self.solution, color='lightgreen', linestyle='-', label='Solution')
        ax.legend()
        
        return fig, ax
