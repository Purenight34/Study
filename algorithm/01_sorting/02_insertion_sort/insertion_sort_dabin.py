# 0 5 6 2 4 1
numbers = list(map(int, input().split()))
n = len(numbers)
for i in range(1,n):
    for j in range(i,0,-1):
        if numbers[j] < numbers[j-1]:
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
        else:
            break

for number in numbers:
    print(number, end=' ')