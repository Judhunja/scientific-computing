from sympy import symbols

# Symbolic function for the encryption process
P, N, e = symbols('P N e')

C = (P ** e) % N

# Modular inverse of P to decrpt message
mod_inv_p = (P % N) ** -1

print(mod_inv_p)

# Substituting P = 7, e = 3, N = 33
sol = C.subs({P: 7, e: 3, N: 33})

print(sol)
