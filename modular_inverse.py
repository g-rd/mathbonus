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
        print(q)

        # Coefficient Si+1 = Si-1 - q*Si
        si = s0 - q * s1
        print(f"s0:{s0} - q:{q} * s1:{s1} = {si}, remainder: {remainder}")
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
    print(results)
    return results


def modular_inverse(a, mod):
    gcd = extended_eucleidian(mod, a)
    return gcd[-2][-1]


inverse = modular_inverse(3, 8)
#
print(inverse)