# line = open('input_DynamicLock.txt')
# n_inp = int(next(line).split()[0])
# N_inp = [int(next(line).split()[0]) for i in range(n_inp)]

n_inp = int(input())
N_inp = [int(input()) for i in range(n_inp)]


def dynamic_lock(n, N):
    pre_sum = {N[0]}
    rest_sum = sum(N[1:]) % 360
    for i in range(1, n):
        if rest_sum in pre_sum:
            return 'YES'
        add_plus = {abs(pre + N[i]) % 360 for pre in pre_sum}
        add_minus = {abs(pre - N[i]) % 360 for pre in pre_sum}
        pre_sum = add_minus.union(add_plus)
        rest_sum = sum(N[i+1:]) % 360

    if (rest_sum in pre_sum) or (0 in pre_sum):
        return 'YES'
    else:
        return 'NO'


print(dynamic_lock(n_inp, N_inp))
