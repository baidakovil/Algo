n_inp, m_inp = map(int, input().split())
import math

def TwoButtons(n,m):
    if m < n:
        return n-m
    power_base = math.ceil(math.log(m/n,2))                 #узнаём степень двойки для превышения m
    remainder = n * 2 ** power_base - m                     #узнаём остаток, т.е. сколько придётся отбавлять
    body_minus = 0                                          #счётчик вычитаемых единиц
    while remainder > 0:
        power_body = math.floor(math.log(remainder, 2))     #узнаем log наибольшего числа, которое хотелось бы скостить единицами
        if power_body > power_base:                         #если число слишком велико, будет скосщать тем, что имеем
            power_body = power_base
        remainder = remainder - 2 ** power_body             #теперь имеем новый остаток, для которого повторим операцию
        body_minus += 1                                     #не забываем добавлять единицы в список нажатий кнопок
    return power_base + body_minus + remainder

print(TwoButtons(n_inp,m_inp))

# for n in range(10000, 10101):
#     print(f'n = 1, m={n}, buttons ={TwoButtons(1,n)}')