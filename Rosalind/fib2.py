def fib1(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    if n == 0:
        return 0

    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1

    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]

x = 22
print fib2(x)
# print fib1(x)
