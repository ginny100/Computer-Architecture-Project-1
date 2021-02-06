def fib1(n = 10):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Normal case
    return fib1(n-1) + fib1(n-2)

# Driver Code
print(fib1(45))
