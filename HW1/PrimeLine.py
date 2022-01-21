import math

def PrimeLine(N):
    primes = []
    firstPrimes = (2,3,5,7,11,13)
    for n in range(2, N + 1):
        maybeprime = True
        if n in firstPrimes:
            primes.append(str(n))
            continue
        else:
            for i in (2,3,5,7,11):
                if n % i == 0 :
                    break
            else:
                lim = math.sqrt(n)
                div = 11
                while div <= lim:
                    div = div + 2
                    if n % div == 0:
                        maybeprime = False
                        break
                    div = div + 4
                    if n % div == 0:
                        maybeprime = False
                        break
                    div = div + 2
                    if n % div == 0:
                        maybeprime = False
                        break
                    div = div + 2
                    if n % div == 0:
                        maybeprime = False
                        break
                if not maybeprime:
                    continue
                else:
                    primes.append(str(n))

    answer = '\n'.join(primes)
    return answer

N = int(input())

print(PrimeLine(N))