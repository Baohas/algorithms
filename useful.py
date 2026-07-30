#region построение приближения на неполных данных
import numpy as np
from scipy.optimize import curve_fit
#линейное приближение - недооценивание операций
def linear_model(x, a, b):
    return a * x + b
#квадратичное приближение - переоценивание операций
def quadratic_model(x, a, b):
    return a * x ** 2 + b * x

#экспериментальные данные
xs = [100, 1000, 10000]
ys = [0.063, 0.565, 5.946]

#первое возвращаемое значение - массив из двух коэффициентов
'''(a, b), _ = curve_fit(linear_model, xs, ys)
print(f"Linear = {a}*N + {b}")
(a, b), _ = curve_fit(quadratic_model, xs, ys)
print(f"Quadratic = {a}*N + {b}")'''
#endregion

