import numpy as np
import matplotlib.pyplot as plt
from typing import Optional, Union

"""
@author Jeremy Hopkins
@author Iris Yang
@version 0.2.1
"""
class FalsePosition():

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
        """Construct `FalsePosition`
        
            Args:
                f: Callable representation of function to be estimated.
                a: Min point value.
                b: Max point value
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
        m = (self.f(self.b) - self.f(self.a))/(self.b - self.a)

        c = self.a - self.f(self.a)/m

        self.count = 0
        self.approx_vals = []
        self.approx_vals.append(c)

        self.solution = self.method(self.f, self.a, self.b, c)
        return self.solution

        
    def method(self, f, a, b, c):
        self.count += 1

        if(np.abs(f(c)) < self.error):
            return c

        if(f(c)*f(a) > 0):
            a = c
        else:
            b = c

        m = (f(b) - f(a))/(b - a)

        c = a - f(a)/m

        self.approx_vals.append(c)

        return self.method(f, a, b, c)


    def plot_solution(self) -> tuple[plt.Figure, plt.Axes]:
        fig, ax = plt.subplots()
        fig.set_size_inches(11, 8.5)
        if self.string_func is not None:
            ax.set_title("False Position Method for " + self.string_func)
        else:
            ax.set_title("False Position Method")
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
        