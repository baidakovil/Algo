# line = open('input_RookBishopKing.txt')
# r1, c1, r2, c2 = map(int, next(line).split())

r1, c1, r2, c2 = map(int, input().split())

drow = abs(r2-r1)
dcolumn = abs(c2-c1)

def Rook(dr, dc):
    if min(dr, dc) == 0: #если стоят на одной прямой, нужен один ход
        return 1
    else:
        return 2 #а иначе два хода

def Bishop(dr, dc):
    if min(dr, dc) == 0: #если стоят на одной прямой, то либо два хода, либо ноль
        if max(dr, dc) % 2 == 0:
            return 2
        else:
            return 0
    elif dr == dc: #если на одной диагонали, то один ход
        return 1
    elif (dr + dc) % 2 == 0: #если не на одной диагонали и не на одной прямой, то два или ноль ходов
        return 2
    else:
        return 0

def King(dr, dc):
    return max(dr, dc)

print(f'{Rook(drow,dcolumn)} {Bishop(drow,dcolumn)} {King(drow,dcolumn)}')