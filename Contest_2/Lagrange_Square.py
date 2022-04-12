# def lagrange(n):
#     for a in range(1,int(n ** 0.5) + 1):
#         t = a * a
#         for b in range(0, a + 1):
#             y = b * b
#             for c in range(0, b + 1):
#                 u = c * c
#                 if n - t - y - u >= 0:
#                     check = (n - t - y - u) ** 0.5
#                     if not check % 1 :
#                         return a, b, c, int(check)
# print(*lagrange(int(input())))

import math

def lagrange(n):
    squad = 0
    power = 1
    check_1 = 0
    for a in range(1,int(n ** 0.5) + 1):
        t = a * a
        squad += 1
        for b in range(0, a + 1):
            y = b * b
            squad += 1
            for c in range(0, b + 1):
                u = c * c
                squad += 1
                if n - t - y - u >= 0:
                    check = (n - t - y - u) ** 0.5
                    power += 1
                    # check_1 += 1
                    if not check % 1 :
                        return a, b, c, int(check), squad + power + check_1

for i in range(98,101):
    answer = lagrange(int(i))
    print(f'i = {i}, log(i)={round(math.log(i),2)},log(iters)={round(math.log(answer[4]),3)},iters={answer[4]}, nums:{ answer[:4] }')