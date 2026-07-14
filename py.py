import numpy as np

def numerical_gradient(f, x):
    h = 1e-4
    grad = np.array([0.0,0.0])

    for i in range(2):
        x[i] += h
        fxh1 = f(x)
        x[i] -= 2*h
        fxh2 = f(x)

        grad[i] = (fxh1 - fxh2) / (2*h)
        x[i] += h
    return grad

def gd(f, x, lr=0.1, num=100):
  for i in range(num):
    x -= lr * numerical_gradient(f, x)
  return x

def func(x):
  return x[0]**2 + x[1]**2

init_x = np.array([-3.0, 4.0]) #초기값
print(gd(func, init_x))