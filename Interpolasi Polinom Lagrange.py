import matplotlib.pyplot as plt
from sympy import symbols, simplify, lambdify

# Data dari gambar
x = [5, 10, 15, 20, 25, 30, 35, 40]
y = [40, 30, 25, 40, 18, 20, 22, 15]

def lagrange_interpolation(x, y):
    n = len(x)
    X = symbols('X')
    polynomial = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (X - x[j]) / (x[i] - x[j])
        polynomial += term
    return simplify(polynomial)

def plot_interpolation(x, y, lagrange_poly):
    # Menghitung nilai x untuk grafik (5 <= x <= 40)
    x_vals = [i/10 for i in range(50, 401)]  # Menghasilkan nilai dari 5.0 hingga 40.0 dengan interval 0.1
    lagrange_func = lambdify(symbols('X'), lagrange_poly, modules=['numpy'])
    
    # Menghitung nilai y berdasarkan polinom Lagrange
    y_vals = [lagrange_func(val) for val in x_vals]
    
    # Membuat plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='red', label='Data Points')  # Plot titik data asli
    plt.plot(x_vals, y_vals, label='Lagrange Interpolation', linestyle='--')  # Plot interpolasi Lagrange
    plt.xlabel('Tegangan, x (kg/mm²)')
    plt.ylabel('Waktu patah, y (jam)')
    plt.title('Interpolasi Polinom Lagrange')
    plt.legend()
    plt.grid(True)
    plt.show()

# Menghitung polinom interpolasi Lagrange
lagrange_poly = lagrange_interpolation(x, y)

# Menampilkan polinom
print(f"Polinom Lagrange: {lagrange_poly}")

# Plot hasil interpolasi
plot_interpolation(x, y, lagrange_poly)
