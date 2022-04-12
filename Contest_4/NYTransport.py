# line = open('input_NYTransport.txt')
# n, t = map(int, next(line).split())
# N = tuple(map(int, next(line).split()))

n, t = map(int, input().split())
N = tuple(map(int, input().split()))

def NY(N_inp, t_inp):
    cellto = 1
    cellfrom = 1
    while cellto < t_inp:
        cellto = cellfrom + N_inp[cellfrom-1]
        if cellto == t_inp:
            return 'YES'
        cellfrom = cellto
    return 'NO'

print(NY(N,t))