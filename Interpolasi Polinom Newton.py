import matplotlib.pyplot as plt
from sympy import symbols, simplify, lambdify

# Data dari gambar
x = [5, 10, 15, 20, 25, 30, 35, 40]
y = [40, 30, 25, 40, 18, 20, 22, 15]

def divided_differences(x, y):
    """Menghitung tabel perbedaan terbagi Newton."""
    n = len(y)
    coef = [0] * n
    for i in range(n):
        coef[i] = y[i]
    
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
    
    return coef

def newton_polynomial(x, y):
    """Menghitung polinom Newton berdasarkan tabel perbedaan terbagi."""
    coef = divided_differences(x, y)
    X = symbols('X')
    n = len(coef)
    polynomial = coef[0]
    product_term = 1
    for i in range(1, n):
        product_term *= (X - x[i-1])
        polynomial += coef[i] * product_term
    return simplify(polynomial)

def plot_interpolation(x, y, newton_poly):
    """Memplot hasil interpolasi polinom Newton."""
    x_vals = [i / 10 for i in range(50, 401)]
    newton_func = lambdify(symbols('X'), newton_poly, modules=['math'])

    y_vals = [newton_func(val) for val in x_vals]

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='red', label='Data Points')
    plt.plot(x_vals, y_vals, label='Newton Interpolation', linestyle='--')
    plt.xlabel('Tegangan, x (kg/mm²)')
    plt.ylabel('Waktu patah, y (jam)')
    plt.title('Interpolasi Polinom Newton')
    plt.legend()
    plt.grid(True)
    plt.show()

# Menghitung polinom interpolasi Newton
newton_poly = newton_polynomial(x, y)

# Menampilkan polinom
print(f"Polinom Newton: {newton_poly}")

# Plot hasil interpolasi
plot_interpolation(x, y, newton_poly)
