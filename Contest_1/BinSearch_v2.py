from operator import itemgetter
import math

line = open('input2.txt')
N, K = map(int, next(line).split())
m1 = tuple(map(int, next(line).split()))
m2 = tuple(map(int, next(line).split()))

def binary2(num):
    lb = 0
    rb = N-1
    dp = rb - lb
    while dp > 1:
        cp = math.floor(lb + (rb-lb)/2)
        pretendent = m1[cp]
        if num < pretendent:
            rb = cp
        else:
            lb = cp
        dp = rb - lb
    vl = m1[lb]
    vr = m1[rb]
    dvl = abs(num-vl)
    dvr = abs(num-vr)
    deltas = ( (dvl, vl),(dvr, vr) )
    answer = sorted(deltas, key=itemgetter(0, 1))[0][1]
    return answer

otvet = '\n'.join([str(binary2(num)) for num in m2])
print(otvet)