#Write two functions that takes as input a number n and
# returns the factorial of that number.
# One function should use loops and other use
# recursion to solve the same.
def factorial_loop(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

print(factorial_loop(3))
print(factorial(5))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

