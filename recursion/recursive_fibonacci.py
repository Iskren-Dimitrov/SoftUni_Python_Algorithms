'''Each member of the Fibonacci sequence is calculated from the sum of the two previous members.\
The first two elements are 1, 1. Therefore the sequence goes as 1, 1, 2, 3, 5, 8, 13, 21, 34…
The following sequence can be generated with an array, but that’s easy, so your task is to implement it recursively.
If the function GetFibonacci(n) returns the nth Fibonacci number, we can express it using\
GetFibonacci(n) = GetFibonacci(n-1) + GetFibonacci(n-2).
However, this will never end and in a few seconds a Stack Overflow Exception is thrown. In order for the recursion\
to stop it has to have a "bottom". The bottom of the recursion is getFibonacci(1), and should return 1.\
The same goes for getFibonacci(0).
'''


def calc_fib(number):
    if number <= 1:
        return 1
    return calc_fib(number - 1) + calc_fib(number - 2)


print(calc_fib(10))
