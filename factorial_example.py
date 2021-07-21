def factorial(n):
    result = 1

    for i in range(1, n+1):
        result *= i

    return result

def factorial_recursive(n):
    result = 1
    if n==0:
        return 1

    result = n * factorial_recursive(n-1)

    return result


print(factorial(5))

print(factorial_recursive(5))