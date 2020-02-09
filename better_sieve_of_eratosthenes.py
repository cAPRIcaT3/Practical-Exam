list_of_primes = []
L2 = []
for I in range(2000):
    list_of_primes.append(1)
for I in range(2,2000):
    if list_of_primes[I]== 1:
        for J in range(I+1,2000):
            if J%I == 0:
                list_of_primes[J]=0
for n in range(len(list_of_primes)):
    if list_of_primes[n]==1:
        print(n)