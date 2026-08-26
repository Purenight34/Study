# input
# 5 2


def backtracking(start, remaining):
    if remaining == 0:
        if numbers[0] == 1 and numbers[-1] == 1:
            return
        print(''.join(map(str, numbers)))
        return

    for i in range(start, n):
        numbers[i] = 1
        backtracking(i+1, remaining-1)
        numbers[i] = 0

n, m = map(int, input().split())
numbers = [0]*n
backtracking(0, m)