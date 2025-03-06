from sympy import symbols, Matrix

A = Matrix([[2, 1], [1, 3]])

det_A = A.det()  # Symbolic determinant

print(det_A)

eigenvals_A = A.eigenvals()  # Get the eigenvalues of A

# Get a characteristic equation for the matrix

x = symbols('x')

fn_1 = A.charpoly(x)

# Convert to expression
exp_1 = fn_1.as_expr()

# Check whether the eigenvalues satisfy the characterstic
# equation for the matrix

# Check only the eigenvalues(keys) and not the multiplicity
for val in eigenvals_A.keys():
    # The characteristic equation should be zero
    # at a given eigenvalue

    # Simplify to avoid minor symbolic inconsistencies
    if not (exp_1.subs(x, val).simplify() == 0):
        print("Does not satisfy the equation")
    else:
        print("satisfies the equation")
