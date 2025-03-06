from sympy import symbols, factor, S, inverse_laplace_transform
from sympy.physics.control.control_plots import pole_zero_numerical_data
from sympy.physics.control.lti import TransferFunction

s, t = symbols('s t')

H = S(1) / (s ** 2 + 3 * s + 2)

# Factor the denominator
factored_denominator = factor(s ** 2 + 3 * s + 2)

print(factored_denominator)

# Inverse Laplace transform of H
inverse_lap = inverse_laplace_transform(H, s, t)

print(inverse_lap)

# Make H a transfer function
tf1 = TransferFunction(1, (s ** 2 + 3 * s + 2), s)

# Get the poles of the system
poles = pole_zero_numerical_data(tf1)

print(poles)
