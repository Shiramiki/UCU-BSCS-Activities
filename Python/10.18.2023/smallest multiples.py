import math

def smallest_multiple(num):
    LCM = 1
    factors = []
    for i in range(num, 1, -1):
        GCD= math.gcd(LCM, i)
        LCM = (LCM * i) // GCD
        factors.append(i)
    factors = factors[0:7]
    return LCM, factors

n = 13
smallest_multiple, factors = smallest_multiple(n)

print(f"Factors: {factors}")
print(f"Smallest Multiple of the first {n} numbers: {smallest_multiple}")
