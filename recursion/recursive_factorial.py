'''Write a program that calculates the recursively factorial of a given number.
Example:
    input: 5 --> output: 120
    input: 10 --> output: 3628800
'''

def calc_fact(n):
    if n == 0:
        return 1
    return n * calc_fact(n - 1)


n = int(input())

print(calc_fact(n))
