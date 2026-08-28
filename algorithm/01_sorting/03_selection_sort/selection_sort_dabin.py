# input
# 2 5 6 13 259 21
# -1 -5 -32 123 59 89
# 2.4 3.1 0.2 2.2 2.4
# 3.1 232.53 232.54 -321.26 294.3

numbers = list(map(float, input().split()))
n = len(numbers)

for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

for number in numbers:
    print(number, end=' ')