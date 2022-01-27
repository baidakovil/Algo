# line = open('input_CutTheTape.txt')
# n_inp, a_inp, b_inp, c_inp = map(int, next(line).split())
n_inp, a_inp, b_inp, c_inp = map(int, input().split())


def cut(n_less, x, y):
    mlt_y = 0
    while mlt_y <= n_less // y:
        mlt_x = (n_less - mlt_y * y) / x
        if mlt_x.is_integer():
            return int(mlt_x + mlt_y)
        mlt_y += 1
    return False


def super_cut(n, abc):
    try_a_b = cut(n, abc[0], abc[1])
    if try_a_b:
        return try_a_b
    a_count = n // abc[0]
    for i in range(n // abc[0] + 1):
        n_less = n - a_count * abc[0]
        try_b_c = cut(n_less, abc[1], abc[2])
        if try_b_c:
            return try_b_c + a_count
        a_count -= 1


print(super_cut(n_inp, sorted([a_inp, b_inp, c_inp])))
