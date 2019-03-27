def fib_slow(n):
    if n <= 2:
        return 1
    else:
        return fib_slow(n - 2) + fib_slow(n - 1)

def fib_fast(a,b,n):
    if n < 3:
        return b
    else:
        return (fib_fast(b,a+b,n-1))