from sympy import symbols, diff, solve

x = symbols('x')

C = 5 * x ** 3 - 10 * x ** 2 + 4 * x + 3

# Find the symbolic derivative
symbolic_derivative = diff(C)

print(symbolic_derivative)

# Solve for x when cost is minimized(function equated to zero)
cost_minimized_x = solve(symbolic_derivative, x)

print(cost_minimized_x)

""" The value of x is always positive when x is minimized
thus making the cost function profitable """
