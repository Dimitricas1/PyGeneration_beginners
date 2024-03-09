n = int(input())
fib_prev_2 = 1
fib_prev_1 = 1

for _ in range(n):
    print(fib_prev_1, end=" ")
    fib_prev_1, fib_prev_2 = fib_prev_2, fib_prev_2 + fib_prev_1
