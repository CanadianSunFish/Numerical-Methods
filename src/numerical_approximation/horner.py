import numpy as np
import matplotlib.pyplot as plt
from typing import Optional, Union

"""
@author Jeremy Hopkins
@author Iris Yang
@version 0.1.3
"""
class Horner():

    def __init__(
        self,
        poly_arr: tuple[int],
        poly_len: int,
        a: int,
        b: int,
        error: float,
        step: Optional[float] = None,
        string_func: Optional[str] = None,
    ):

        self.poly_arr = poly_arr

        assert isinstance(poly_len, int), "poly_degrees must be an int"
        self.poly_len = poly_len

        assert isinstance(b, (float, int)), "a must be a float or an int"
        self.a = a

        assert isinstance(b, (float, int)), "b must be an int"
        self.b = b

        assert(a < b), "min point must be smaller than max point"

        assert isinstance(error, float), "error must be a float"
        self.error = error

        if string_func is not None:
            assert isinstance(string_func, str), "string_func must be string representation of polynomial" 
        self.string_func = string_func

        if step is None:
            step = 0.1
        assert isinstance(step, float), "step must be float value"
        self.step = step


    def solve(self):
        eval_array = np.arange(self.a, self.b, self.step)
        result_arr = self._horner_eval(eval_array)

        return eval_array, result_arr


    def _horner_eval(self, eval_array):
        
        result_arr = []

        for x in eval_array:
            result = self.poly_arr[0]
            for j in range(1, self.poly_len):
                result = result * x + self.poly_arr[j]
            result_arr.append(result)

        return result_arr


    def plot_solution(self, x, y):
        fig, ax = plt.subplots()
        fig.set_size_inches(11, 8.5)
        if self.string_func is not None:
            ax.set_title("Horner Method for " + self.string_func)
        else:
            ax.set_title("Horner Method")
        ax.set_xlabel("x-axis")
        ax.set_ylabel("y-axis")
        ax.plot(x, y, label='Polynomial')
        for i in range(len(y)):
            y_plot = y[i]
            if (y_plot > -self.error and y_plot < self.error):
                x_plot = x[i]
                ax.scatter(x_plot, y_plot, s=10, label='Zeros')
        ax.legend(loc='upper center')
        
        return fig, ax
