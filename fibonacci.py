def fibonacci(n):
    fib = 0, 1
    for i in range(n):
        fib = fib[1], sum(fib)
    return fib[0]

if __name__ == "__main__":
    print([fibonacci(i) for i in range(10)])
        
