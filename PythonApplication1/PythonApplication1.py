def fib(n=5):
    """
    Print fibonacci sequence from 1 to n
    use fib.__doc__ to print this documentation
    """
    result = []
    a,b = 0,1
    while a < n:
        result.append(a + b)
        a, b = b, a + b
    return result

print(fib())
