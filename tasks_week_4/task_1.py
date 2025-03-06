from sympy import symbols, expand, factor, simplify, diff, integrate, solve, Matrix

x = symbols('x')

L = (3 * (x ** 2)) + (2 * x) - 5  # The equation defined

# Getting the gradient of L(x)

differentiated_func = diff(L)

print(differentiated_func)

# Gradient when x is zero(Optimal solution)

func_subs_2 = differentiated_func.subs(x, 0)

print(func_subs_2)

second_derivative = diff(differentiated_func)

# Find the turning points by substituting the
# optimal solution into the second derivative

tp = solve(second_derivative, func_subs_2)

# Check for max or min turning point

tp = second_derivative.subs(x, func_subs_2)

if tp < 0:
    print("It is a maximum turning point")
elif tp == 0:
    print("It is a point of inflection")
elif tp > 0:
    print("It is a minimum turning point")
