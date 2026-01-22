import math
def extended_gcd(a, b):
    """
    Returns (gcd, x, y) such that ax + by = gcd(a, b).
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

p = 26513
q = 32321

gcd_val, u, v = extended_gcd(p, q)

print(f"GCD({p}, {q}) = {gcd_val}")
print(f"u = {u}")
print(f"v = {v}")
print(f"Verification: {p}*({u}) + {q}*({v}) = {p*u + q*v}")
