import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
from typing import Optional, Union

"""
@author Jeremy Hopkins
@author Iris Yang
@version 0.2.1
"""
class Steffensen():

    def __init__(
        self, 
        f: callable, 
        x: Union[int, float], 
        error: Optional[Union[int, float]] = None,
        string_func: Optional[str] = None,
        func_solution: Optional[float] = None,
        txt_pos: Optional[str] = 'bottom right'
    ):
        """Construct `Steffensen`
        
            Args:
                f: Callable representation of function to be estimated.
                x: Starting value.
                error: Error bounds.
                string_func: String representation of function being estimated.
                func_sol: The true soltion to the function.
                txt_pos: Positioning for txt plotting.

        """

        self.count = 0
        self.approx_vals = []
        self.solution = 0

        assert callable(f), "f must be callable"
        self.f = f

        assert isinstance(x, (int, float)), "x must be int or float"
        self.x = x

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

        self.solution = self.method(self.f, self.x)
        return self.solution

        
    def method(self, f, x):

        self.count += 1

        if(np.abs(f(x)) < self.error):
            return x
        
        g = f(x + f(x))/f(x) - 1

        x_n = x - f(x)/g

        self.approx_vals.append(x_n)

        return self.method(f, x_n)


    def plot_solution(self) -> tuple[plt.Figure, plt.Axes]:
        fig, ax = plt.subplots()
        fig.set_size_inches(11, 8.5)
        if self.string_func is not None:
            ax.set_title("Steffensen Method for " + self.string_func)
        else:
            ax.set_title("Steffensen Method")
        ax.set_xlabel("Num Computations")
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
        
