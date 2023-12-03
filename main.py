
from scipy import integrate
import  numpy as np 
import plotly.graph_objects as go

"""
Для начала надо найти ограничения чтобы вставить их в формулу объема с тройным интегралом
Нарисуем график:
"""


theta = np.linspace(0, 2 * np.pi, 100)
z_cylinder = np.linspace(-10, 10, 100)
theta_grid, z_grid = np.meshgrid(theta, z_cylinder)
x_cylinder = np.sqrt(50) * np.cos(theta_grid)
y_cylinder = np.sqrt(50) * np.sin(theta_grid)

x = np.linspace(-10, 10, 1000)
y = np.sqrt(5 * x)
z = 3 * x / 11


fig = go.Figure()


fig.add_trace(go.Surface(x=x_cylinder, y=y_cylinder, z=z_grid, colorscale='Blues', showscale=False, opacity=0.8))


fig.add_trace(go.Scatter3d(x=x, y=y, z=np.zeros_like(x), mode='lines', line=dict(color='blue'), name='Curve: y = sqrt(5x)'))


fig.add_trace(go.Scatter3d(x=x, y=np.zeros_like(x), z=z, mode='lines', line=dict(color='green'), name='Curve: z = 3x/11'))


fig.add_trace(go.Scatter3d(x=x, y=np.zeros_like(x), z=np.zeros_like(x), mode='lines', marker=dict(color='purple'), name='y = 0'))
fig.add_trace(go.Scatter3d(x=np.zeros_like(x), y=np.zeros_like(x), z=z, mode='lines', marker=dict(color='purple'), name='z = 0'))
fig.add_trace(go.Scatter3d(x=np.ones_like(x) * 5, y=np.linspace(-10, 10, 1000), z=np.zeros_like(x), mode='lines', line=dict(color='red'), name='Curve: x = 5'))


fig.update_layout(scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'), title='РГР 2')


fig.show()

"""
Найдем объем фигуры до x = 5 и объем фигуры где x:[5;5sqrt(2)] и сложим для получения общего объема
"""




x_l = 5*np.sqrt(2)

x = 5

y_l = np.sqrt(5 * x);
z_l = 3 * x/11;


#Считаем тройной интеграл с помощью библиотеки scipy
f = lambda z, y, x: 1

result_1 = integrate.tplquad(f, 0, x, 0, y_l, 0, z_l)
result_2 = integrate.tplquad(f, 5, x_l, 0, y_l, 0, z_l)

print(result_1[0] + result_2[0])

