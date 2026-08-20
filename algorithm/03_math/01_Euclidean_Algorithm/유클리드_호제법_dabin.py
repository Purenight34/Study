# 1071 1029
'''
이 문제는 유클리드 호제법을 파이썬 알고리즘으로 구현하는 문제이다.
    유클리드 호제법이란 두 수의 최소공약수를 구하는 알고리즘이다.
    이 문제에서는 입력으로 두 자연수가 주어지고,
    결과로 입력받은 두 수의 최소공약수를 출력한다.
'''
a, b = map(int, input().split())

max_num = max(a,b)
min_num = min(a,b)

res = 0

while min_num != 0:
    res = max_num % min_num
    max_num = min_num
    min_num = res

print(max_num)
