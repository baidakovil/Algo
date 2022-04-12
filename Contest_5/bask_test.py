from random import *

bask_test = open('bask_test.txt', mode='w')
n = randint(1, 100)
bask_test.write(str(n))
bask_test.write('\n')
a = list()
b = list()
for i_2 in range(n):
    a_num = randint(1, 100)
    b_num = randint(1, 100)
    a.append(a_num)
    b.append(b_num)
bask_test.write(' '.join(str(i) for i in a))
bask_test.write('\n')
bask_test.write(' '.join(str(i) for i in b))
bask_test.close()
