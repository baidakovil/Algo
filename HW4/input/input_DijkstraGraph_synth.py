from random import random

n = 99999
m = 99999

with open('input_DijkstraGraph_synth.txt', mode='w') as output_file:
    print(f'{n} {m}', file=output_file)
    for i in range(1,m):
        print(f'{i} {i+1} {int(random()*1000)}', file=output_file)