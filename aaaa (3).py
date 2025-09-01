import numpy as np

def f_segment_1(x):
    return np.exp(-x) / np.sqrt(3 * x - x**2)

def trapezoidal_segment_1(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f_segment_1(x)
    integral = h * ((y[0] + y[-1]) / 2 + np.sum(y[1:-1]))
    return integral

def simpson_segment_1(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f_segment_1(x)
    integral = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2])
    integral *= h / 3
    return integral

def f_transformed(t):
    x = (3 / 2) * (1 - np.cos(t)) 
    return np.exp(-x) 

def trapezoidal_integral(a, b, n):
    t = np.linspace(a, b, n + 1) 
    h = (b - a) / n  
    y = f_transformed(t)  
    integral = h * ((y[0] + y[-1]) / 2 + np.sum(y[1:-1]))
    return integral

def simpson_integral(a, b, n):
    t = np.linspace(a, b, n + 1)  
    h = (b - a) / n  
    y = f_transformed(t) 
    integral = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2])
    integral *= h / 3
    return integral

a1, b1 = 1, 2
n_values_12 = [2**i for i in range(2, 7)]  
n_values_12.extend([1000, 10000])  

a2, b2 = 0, np.pi 
n_values_03 = [8, 16, 32, 64, 1000, 10000] 

trapz_12_results = []
simpson_12_results = []

for n in n_values_12:
    trapz = trapezoidal_segment_1(a1, b1, n)
    simpson = simpson_segment_1(a1, b1, n)
    trapz_12_results.append(trapz)
    simpson_12_results.append(simpson)

trapz_03_results = []
simpson_03_results = []

for n in n_values_03:
    trapz = trapezoidal_integral(a2, b2, n)
    simpson = simpson_integral(a2, b2, n)
    trapz_03_results.append(trapz)
    simpson_03_results.append(simpson)

print("Результаты вычисления интегралов:")
print("n\t[1,2] Трапеций\t[1,2] Симпсона\t[0,3] Трапеций\t[0,3] Симпсона")
for i, n in enumerate(n_values_12):
    trapz_12 = trapz_12_results[i]
    simpson_12 = simpson_12_results[i]
    if n in n_values_03:
        idx = n_values_03.index(n)
        trapz_03 = trapz_03_results[idx]
        simpson_03 = simpson_03_results[idx]
        print(f"{n}\t{trapz_12:.10f}\t{simpson_12:.10f}\t{trapz_03:.10f}\t{simpson_03:.10f}")
    else:
        print(f"{n}\t{trapz_12:.10f}\t{simpson_12:.10f}\t-\t-")
