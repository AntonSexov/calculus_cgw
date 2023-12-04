import numpy as np


#функция для расчета интеграла  методом прямоугольников
def triple_integral_approx(f, x_range, y_range, z_range, num_points=100):
    x_min, x_max = x_range
    y_min, y_max = y_range
    z_min, z_max = z_range
    
    x_values = np.linspace(x_min, x_max, num_points)
    y_values = np.linspace(y_min, y_max, num_points)
    z_values = np.linspace(z_min, z_max, num_points)
    
    dx = x_values[1] - x_values[0]
    dy = y_values[1] - y_values[0]
    dz = z_values[1] - z_values[0]
    
    integral_sum = 0.0
    
    for x in x_values:
        for y in y_values:
            for z in z_values:
                integral_sum += f(x, y, z) * dx * dy * dz
    
    return integral_sum

def triple_integral_1(a, b, c, d, e, f):
    volume = (b - a) * (d - c) * (f - e)
    return volume