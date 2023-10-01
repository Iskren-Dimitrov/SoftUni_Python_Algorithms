'''Write a program that simulates the execution of n nested loops from 1 to n which prints the values\
of all its iteration variables at any given time on a single line. Use recursion'''


def nested_loops(idx, arr):
    if idx >= len(arr):
        print(*arr, sep=' ')
        return

    for num in range(1, len(arr) + 1):
        arr[idx] = num
        nested_loops(idx + 1, arr)


n = int(input())
arr = [None] * n

nested_loops(0, arr)
