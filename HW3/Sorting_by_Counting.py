data = list(map(int, open('input_Sorting_by_Counting.txt').readline().split()))

def CountSort(A):
    tableu = [0 for i in range(0,101)]
    for char in A:
        tableu[int(char)] += 1
    A.clear()
    for i in range(0,101):
        A += list([i]*tableu[i])
    return A

with open('output_Sorting_by_Counting.txt', mode='w') as output_file:
     print(*CountSort(data),file=output_file)

# data = list(map(int, open('input_Sorting_by_Counting.txt').readline().split()))
# import math
#
# def CountSort(A):
#     tableu = [0]*101
#     iters = 0
#     for char in A:
#         tableu[int(char)] += 1
#         iters += 1
#     A.clear()
#     for i in range(0,101):
#         A += list([i]*tableu[i])
#         iters += 1
#     return A,iters
#
# answer = CountSort(data)
# n = len(data)
#
# print(f'n = {n}, log(n)={round(math.log(n))},log(iters)={round(math.log(answer[1]),3)},iters={answer[1]}')