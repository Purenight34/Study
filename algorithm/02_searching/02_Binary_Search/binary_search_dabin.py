# input
# 4 5 6 7 8 9 10 11 12
# 5

# output
# 1
# 2

numbers = list(map(int, input().split()))
k = int(input())
n = len(numbers)

left = 0
right = n-1
cnt = 0
is_sorted = True
found = False

for i in range(n-1):
    if numbers[i] > numbers[i+1]:
        is_sorted = False
        break

if not is_sorted:
    print('없음')
    print(cnt)
else:
    while left <= right:
        mid = (left + right)//2
        if numbers[mid] == k:
            cnt += 1
            print(mid)
            print(cnt)
            found = True
            break

        elif numbers[mid] < k:
            left = mid+1
            cnt += 1
        else:
            right = mid-1
            cnt += 1

if not found and is_sorted:
    print('없음')
    print(cnt)