# n_inp = int(input())
# a_inp = tuple(map(int, input().split()))
# b_inp = tuple(map(int, input().split()))

from random import *


def basketball(n, a_row, b_row):
    # profit = [0] цена инвертирования каждой пары, (индекс - номер пары)
    # pointer True/False указатель на предыдущую пару: если был выбран a, то равен True
    # nulls перечень ячеек, в которых игрок не выбран
    # height текущая суммарная высота игроков

    def judge():
        def invert_and_fill():
            profit[last_null_pos] = bonus_profit
            height[last_null_pos] = bonus
            nulls.pop()
            for a in range(last_null_pos + 1, i_1):
                height[a] -= profit[a]
                profit[a] = -profit[a]

        def invert_from_zero():
            for a in range(i_1):
                height[a] -= profit[a]
                profit[a] = -profit[a]

        def insert_null():
            nulls.append(best_choice[1])
            for a in range(best_choice[1], i):
                height[a] -= profit[a]
                profit[a] = -profit[a]
            profit[best_choice[1]] = height[best_choice[1]]
            height[best_choice[1]] = 0

        i_1 = i
        variants = list([(-1, -1)])
        if len(nulls) > 0:
            last_null_pos = nulls[-1]
            if (i_1 - last_null_pos) % 2 == 1:
                bonus_row = not select[0][1]
            else:
                bonus_row = select[0][1]
            if bonus_row:
                bonus = a_row[last_null_pos]
                bonus_profit = a_row[last_null_pos] - b_row[last_null_pos]
            else:
                bonus = b_row[last_null_pos]
                bonus_profit = b_row[last_null_pos] - a_row[last_null_pos]
            variant = delta - sum(profit[last_null_pos + 1:]) + bonus
            if variant > 0:
                variants.append((variant, last_null_pos))
        else:
            variant = delta - sum(profit)
            if variant > 0:
                variants.append((variant, 0))

        i_2 = i
        changed_profit = 0
        while (delta - changed_profit) > 0 and (i_2 > 1) and ((i_2 + 1) not in nulls):
            i_2 -= 1
            changed_profit = sum(profit[i_2 + 1:])
            variant = delta - changed_profit - height[i_2]
            if variant > 0:
                variants.append((variant, i_2))
        best_choice = max(variants)
        if best_choice[0] > 0:
            if len(nulls) and (best_choice[1] == nulls[-1]):
                invert_and_fill()
            elif best_choice[1] == 0:
                invert_from_zero()
            else:
                insert_null()
            return False
        else:
            return True

    height = list()
    profit = list()
    nulls = list()

    for i in range(0, n):
        select = sorted(((a_row[i], True), (b_row[i], False)), reverse=True)  # берем очередную пару и выбираем
        # большее число
        delta = select[0][0] - select[1][0]
        if (i > 0) and (select[0][1] == pointer):  # разветвляем, начиная со второй пары: если выбор = предыдущий
            if judge():  # судья говорит True, если нужно поменять решение
                height.append(select[1][0])  # изменение выбора и добавляем в height другой вариант
                profit.append(-delta)
                pointer = not select[0][1]
                continue  # и берём следующую пару
        height.append(select[0][0])  # иначе просто кладём выбранное значение в height
        profit.append(delta)  # и добавляем значение в profit
        pointer = select[0][1]

    return height


def generate():
    bask_test = open('bask_test.txt', mode='w')
    n = randint(1, 10)
    bask_test.write(str(n))
    bask_test.write('\n')
    a = list()
    b = list()
    for i_2 in range(n):
        a_num = 1
        b_num = randint(1, 1000)
        a.append(a_num)
        b.append(b_num)
    bask_test.write(' '.join(str(i) for i in a))
    bask_test.write('\n')
    bask_test.write(' '.join(str(i) for i in b))
    bask_test.close()


def write_answer():
    generate()
    line = open('bask_test.txt', mode='r')
    n_inp = int(next(line))
    a_inp = tuple(map(int, next(line).split()))
    b_inp = tuple(map(int, next(line).split()))
    line.close()
    answer = basketball(n_inp, a_inp, b_inp)
    with open("bask_test_input.csv", "a") as mile:
        mile.write(','.join(str(i) for i in a_inp))
        mile.write('\n')
        mile.write(','.join(str(i) for i in b_inp))
        mile.write('\n')
        mile.write('\n')

    with open("bask_test_answer.csv", "a") as mile:
        stringgg = ','.join(str(i) for i in answer)
        mile.write(stringgg)
        mile.write('\n')
        mile.write('\n')
        mile.write('\n')


for i in range(10):
    write_answer()
