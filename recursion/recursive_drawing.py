'''Write a program that draws the figure below depending on n.'''


def draw_figure(n):
    if n == 0:
        return

    print('*' * n)
    draw_figure(n - 1)
    print('#' * n)


n = int(input())
draw_figure(n)
