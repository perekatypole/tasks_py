import matplotlib.pyplot as plt

def func(x):
    return x**2 + 2*x - 3

x_value = 4
y_value = func(x_value)

plt.plot(x_value, y_value, 'ro')
plt.plot(range(-10, 11), [func(x) for x in range(-10, 11)])
plt.show()