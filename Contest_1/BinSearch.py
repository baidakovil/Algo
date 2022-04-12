from operator import itemgetter

file = open('input4.txt')
line1 = file.readline()
N, K = map(int, line1.split())
line2 = file.readline()
m1 = tuple(map(int, line2.split()))
line3 = file.readline()
m2 = tuple(map(int, line3.split()))

def binary(num):
    if num <= min_m1:
        return min_m1
    elif num >= max_m1:
        return max_m1
    else:
        dif_pos = 2
        left_border = 0
        right_border = N
        claim1_left, claim1_right, dif_val1_right, dif_val1_left, dif_val_dop, val_dop, minimalistic = None, None, None, None, None, None, None
        trigger = False

        while dif_pos > 0:
            if (right_border - left_border) < 2:
                pos0 = left_border
            else:
                pos0 = round( left_border + (right_border-left_border)/2 )
            claim0 = m1[pos0]
            dif_val0 = abs(num-claim0)
            if minimalistic is None:
                minimalistic = dif_val0
            else:
                if dif_val0 < minimalistic:
                    minimalistic = dif_val0

            if trigger:
                if right_border == 2:
                    val_dop = m1[1]
                    dif_val_dop = abs(num - m1[1])
                difs = (dif_val1_left, claim1_left), (dif_val1_right, claim1_right), (dif_val0, claim0),(prev_dif_val0,prev_claim0),(dif_val_dop,val_dop)
                difcleared = (i for i in difs if i[0] is not None)
                preresult = sorted(difcleared, key=lambda dif: dif[0])[0][0]
                if preresult > minimalistic:
                    trigger = False
                    continue
                result1 = sorted(difcleared, key=itemgetter(0, 1))
                return result1[0][1]

            if num == claim0:
                return claim0
            elif num < claim0:
                right_border = pos0
                if (right_border-left_border) < 2:
                    left_pos1 = left_border
                else:
                    left_pos1 = round( left_border + (right_border-left_border)/2 )
                claim1_left = m1[left_pos1]
                dif_val1_left = abs(num-claim1_left)
                if dif_val1_left < minimalistic:
                    minimalistic = dif_val1_left
                if num == claim1_left:
                    return claim1_left
                elif num < claim1_left:
                    right_border = left_pos1
                else:
                    left_border = left_pos1
            elif num > claim0:
                left_border = pos0
                right_pos1 = round( left_border + (right_border-left_border)/2 )
                claim1_right = m1[right_pos1]
                dif_val1_right = abs(num-claim1_right)
                if dif_val1_right < minimalistic:
                    minimalistic = dif_val1_right
                if num == claim1_right:
                    return claim1_right
                if num < claim1_right:
                    right_border = right_pos1+1
                else:
                    left_border = right_pos1-1
            dif_pos = right_border - left_border
            if dif_pos <= 2:   #!!!!
                trigger = True
            prev_claim0 = claim0
            prev_dif_val0 = dif_val0

min_m1 = m1[0]
max_m1 = m1[-1]

otvet = '\n'.join([str(binary(num)) for num in m2])
print(otvet)