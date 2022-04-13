# line = open('input_CutTheTape.txt')
# n_inp, a_inp, b_inp, c_inp = map(int, next(line).split())
n_inp, a_inp, b_inp, c_inp = map(int, input().split())


def cut(n_less, x, y):
    mlt_y = 0
    while mlt_y <= n_less // y:
        mlt_x = (n_less - mlt_y * y) / x
        if mlt_x.is_integer():
            return int(mlt_x), int(mlt_y)
        mlt_y += 1
    return False


def super_cut(n, abc):
    results = []
    a_count = n // abc[0]
    for i in range(a_count + 1):
        try_b_c = cut(n - a_count * abc[0], abc[1], abc[2])
        if try_b_c: results.append(a_count + sum(try_b_c))
        a_count -= 1
    return max(results)


print(super_cut(n_inp, sorted([a_inp, b_inp, c_inp])))
