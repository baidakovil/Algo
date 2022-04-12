from operator import itemgetter

line = open('input_Basketball.txt')
n_inp = int(next(line))
a_inp = tuple(map(int, next(line).split()))
b_inp = tuple(map(int, next(line).split()))


def basketball(n, a, b):

    def change(selected, height, risk, i):
        while i > 0:
            if selected[i]:
                selected[i] = False
                height[i] = b[i]
                risk += 2 * (b[i] - a[i])
            else:
                selected[i] = True
                height[i] = a[i]
                risk += 2 * (b[i] - a[i])
            if selected[i] is None:
                selected[i] == 
            i -= 1
        return selected, height, risk

    def court(selected, select, i):
        if i == 1:
            if (select[0][0] - select[1][0]) > abs(a[0] - b[0]):
                return True
            else:
                return False
        # return True
        return False

    risk = 0
    selected = [0 for i in range(n)]
    height = [0 for i in range(n)]
    for i in range(0, n):
        select = sorted(((a[i], True), (b[i], False)), reverse=True)
        if (i > 0) and (select[0][1] == selected[i - 1]):
            if court(selected, select, i):
                selected, height, risk = change(selected, height, risk, i)
                continue
            else:
                height[i] = select[1][0]
                selected[i] = select[1][1]
                continue
        height[i] = select[0][0]
        selected[i] = select[0][1]
        risk += select[0][0] - select[1][0]

    return sum(height)


print(basketball(n_inp, a_inp, b_inp))
