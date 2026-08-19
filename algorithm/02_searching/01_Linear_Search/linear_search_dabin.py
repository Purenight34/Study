# 5
# 1 2 3 4 5
# 2

n = int(input()) 
numbers = list(map(int, input().split()))
k = int(input())

for i in range(n):
    if numbers[i] == k:
        print(i)
        break
else:
    print('없음')
