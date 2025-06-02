from functools import lru_cache

def factorial(n):
    if n == 0: # базовий випадок
        return 1
    else:
        return n * factorial(n-1) # рекурсивний випадок
print(factorial(10)) # виведе 120


def fibonacci_old(n):
    if n <= 1: # базовий випадок
        return n
    else:
        return fibonacci_old(n-1) + fibonacci_old(n-2) # рекурсивний випадок
print(fibonacci_old(50)) # виведе 55

# def fibonacci_memo(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     else:
#         value = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
#         memo[n] = value
#         return value
# print(fibonacci_memo(500)) # виведе 55

@lru_cache(maxsize=None)  # Unbounded cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(50))  # виведе 55

