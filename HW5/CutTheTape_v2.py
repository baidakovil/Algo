# line = open('input_CutTheTape.txt')
# n_inp, a_inp, b_inp, c_inp = map(int, next(line).split())
n_inp, a_inp, b_inp, c_inp = map(int, input().split())
abc_inp = list(sorted((a_inp, b_inp, c_inp)))


def cut_the_tape(n, a, b, c):
    lvl = 0
    abc = sorted([a, b, c])
    mlt = [n // abc[0], 0, 0]
    while n - abc[0] * mlt[0] - abc[1] * mlt[1] - abc[2] * mlt[2] != 0:
        mlt[0] = n // abc[0]
        mlt[1] = 0
        lvl = min(lvl + 1, 2)
        if lvl == 2:
            mlt[2] += 1
        rest = n - abc[0] * mlt[0] - abc[1] * mlt[1] - abc[2] * mlt[2]
        while (mlt[0] > 0) and (rest != 0):
            mlt[0] = max(0, mlt[0] - 1)
            rest = n - abc[0] * mlt[0] - abc[1] * mlt[1] - abc[2] * mlt[2]
            if rest >= abc[1]:
                mlt[1] += 1
            rest = n - abc[0] * mlt[0] - abc[1] * mlt[1] - abc[2] * mlt[2]
    return sum(mlt)


print(cut_the_tape(n_inp, a_inp, b_inp, c_inp))