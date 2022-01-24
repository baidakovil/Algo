# line = open('input_MaxSequence.txt')
# n = int(next(line))
# a = tuple(map(int, next(line).split()))
n = int(input())
a = tuple(map(int, input().split()))

sequence = 1
max_sequence = 1
i = 0

while i < n-1:
    try:
        sequence = 1
        while a[i+1] >= a[i]:
            i += 1
            sequence += 1
        max_sequence = max(sequence, max_sequence)
        i += 1
    except IndexError:
        continue

print(max(sequence, max_sequence))