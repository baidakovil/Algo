# line = open('input_CutTheTape.txt')
# n_inp, a_inp, b_inp, c_inp = map(int, next(line).split())
n_inp, a_inp, b_inp, c_inp = map(int, input().split())
abc_inp = list(sorted((a_inp, b_inp, c_inp)))


def try_b(n, abc, a_count, c_count, remainder):
    a, b, c = abc[0], abc[1], abc[2]
    b_count_max = (n - c * c_count) // b
    b_count = 0
    while b_count < b_count_max:
        b_count += 1
        remainder = (n - b * b_count - c * c_count)
        if remainder % a == 0:
            a_count = remainder // a
            break
    return a_count, b_count, c_count, remainder


def cut_the_tape(n, abc):
    a, b, c = abc[0], abc[1], abc[2]
    a_count = n // a
    if n % a == 0:
        return a_count
    a_count -= 1
    b_count = 0
    c_count = 0
    remainder = n - a * a_count
    if (b - remainder) % a == 0:
        a_count, b_count, c_count, remainder = try_b(n, abc, a_count, c_count, remainder)
        if remainder % a == 0:
            return a_count + b_count
    for i in range(0, n // c):
        while remainder % a != 0:
            c_count += 1
            a_count, b_count, c_count, remainder = try_b(n, abc, a_count, c_count, remainder)
        return a_count + b_count + c_count


print(cut_the_tape(n_inp, abc_inp))
