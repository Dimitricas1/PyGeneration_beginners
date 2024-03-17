import time
from math import pow

start = time.process_time_ns()
stop = False

for i in range(1, 151):
    if stop:
        break
    for j in range(1, 151):
        print(i, j, sep=", ")
        if stop:
            break
        if j == i:
            continue
        for k in range(1, 151):
            if stop:
                break
            if k == i or k == j:
                continue
            for l in range(1, 151):
                if l == i or l == j or l == k:
                    continue
                summ = i**5 + j**5 + k**5 + l**5
                summ = pow(summ, 1 / 5)
                if (
                    # summ != i
                    # and summ != j
                    # and summ != k
                    # and summ != l
                    summ.is_integer()
                ):
                    print(i, j, k, l, summ)
                    stop = True
                    break

finish = time.process_time_ns()
print(finish - start)
