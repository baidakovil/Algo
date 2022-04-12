a = int(input())
b = int(input())

# a = 1071
# b = 462

def gcd(a, b):
    def remainder(big_r, small_r):
        r = 1
        x = big_r - r * small_r
        while x > small_r:
            x = big_r - r*small_r
            r += 1
        return x

    big_e = max(a, b)
    small_e = min(a, b)
    if small_e == 0:
        return big_e

    while big_e != small_e:
        remain = remainder(big_e, small_e)
        big_e = small_e
        small_e = remain
    return small_e

answer = gcd(a, b)

print(answer)