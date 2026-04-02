def lcm(a, b, n=None):
    if n is None:
        n = max(a, b)
    if n % a == 0 and n % b == 0:
        return n
    return lcm(a, b, n+1)

print(lcm(4, 6))