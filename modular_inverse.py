from math import gcd


def extended_eucleidian(a, b):
    results = list()

    # To begin we know that s1 = 1, s2 = 0 and t1 = 0 and t2 = 1
    s1 = 1
    t1 = 0
    s2 = 0
    t2 = 1

    def recursive(left, remainder):
        nonlocal s2
        nonlocal s1
        nonlocal t1
        nonlocal t2

        # Python way to divide without remainder
        q = left // remainder
        # Coefficient s_i+2 = s_i - q*s_i+1
        si = s1 - q * s2
        s1 = s2
        s2 = si

        # Coefficient t_i+2 = ti - q*ti_+1
        ti = t1 - q * t2
        t1 = t2
        t2 = ti

        new_remainder = left % remainder
        left = q * remainder + new_remainder

        results.append([left, q, remainder, new_remainder, s2, t2])
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


inverse = modular_inverse(3, 8)
print(f"inverse: {inverse}")