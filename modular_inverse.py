from math import gcd


def extended_eucleidian(a, b):
    results = list()

    # To begin we know that S1 = 1, S2 = 0 and T1 = 0 and T2 = 1
    s0 = 1
    t0 = 0
    s1 = 0
    t1 = 1

    def recursive(left, remainder):
        nonlocal s1
        nonlocal s0
        nonlocal t0
        nonlocal t1

        # Python way to divide without remainder
        q = left // remainder
        # Coefficient Si+1 = Si-1 - q*Si
        si = s0 - q * s1
        # print(f"s0:{s0} - q:{q} * s1:{s1} = {si}, remainder: {remainder}")
        s0 = s1
        s1 = si

        # Coefficient Ti+1 = Ti-1 - q*Ti
        ti = t0 - q * t1
        t0 = t1
        t1 = ti

        new_remainder = left % remainder
        left = q * remainder + new_remainder

        results.append([left, q, remainder, new_remainder, s1, t1])
        if new_remainder != 0:
            recursive(remainder, new_remainder)

    recursive(a, b)
    return results


def modular_inverse(a, mod):
    _gcd = extended_eucleidian(mod, a)
    if not _gcd[-1][2] == 1:
        # there exists an inverse only if the numbers are relatively prime.
        print("There is no inverse")
        return None
    else:
        if _gcd[-2][-1] < 0:
            # return a positive inverse.
            return mod + _gcd[-2][-1]
        return _gcd[-2][-1]


inverse = modular_inverse(4, 177)
print(f"inverse: {inverse}")