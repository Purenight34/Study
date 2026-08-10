'''
    이 문제는 유클리드 호제법을 파이썬 알고리즘으로 구현하는 문제이다.
    유클리드 호제법이란 두 수의 최소공약수를 구하는 알고리즘이다.
    이 문제에서는 입력으로 두 자연수가 주어지고,
    결과로 입력받은 두 수의 최소공약수를 출력한다.

'''

'''
    알고리즘 의사코드
    
    txt파일의 두 자연수를 리스트로 입력받는다.
    두 자연수 중 큰 값과 작은 값을 구분한다.
    나머지가 0일때 나눈 값을 할당할 변수 생성.(second_remainer)
    나머지가 0일때 멈추기 위해 나머지를 받아줄 변수 생성.(remainer)
    반복문 사용
    if 문을 이용해 큰 값을 작은 값으로 나눌 때 big이 크면 small로 나눈 뒤 big에 나머지를 재할당
    small이 크면 big으로 나눈 뒤 나머지를 small에 재할당
    동시에 second_remainer에는 나누기 하는 값을 할당
    remainer에는 나머지를 할당
    이후 remainer가 0이 되면 반복을 끝내고 second_remainer를 최소공약수로 출력

'''





import sys

#실행코드
# 표준 입력을 키보드가 아닌 'data.txt' 파일로 변경
sys.stdin = open("test01.txt", "r")

# 기존 코드 그대로 사용 가능
number_list = list(map(int, input().split()))
big_number = max(number_list)
small_number = min(number_list)
remainder = 1
second_remainder = 0
while remainder > 0:
    if small_number > big_number:
        remainder = small_number % big_number
        small_number = remainder
        second_remainder = big_number
    elif big_number > small_number:
        remainder = big_number % small_number
        big_number = remainder
        second_remainder = small_number

print(f"최소공약수는: {second_remainder}")