'''
    이 문제는 유클리드 호제법을 파이썬 알고리즘으로 구현하는 문제이다.
    유클리드 호제법이란 두 수의 최소공약수를 구하는 알고리즘이다.
    이 문제에서는 입력으로 두 자연수가 주어지고,
    결과로 입력받은 두 수의 최소공약수를 출력한다.

'''

"""
요구사항
최대공약수를 gcd 해주세요.
직접 비교하기 귀찮으면 코드 짜라고 한 곳만 건드리기.
직접 비교할거면 다지우고 해도 됨
유클리드 호제법.py 파일이 보이는 곳에서 vs code 켜기
"""
import sys

#실행코드
# 표준 입력을 키보드가 아닌 'data.txt' 파일로 변경
for i in range(4):
    sys.stdin = open(f"tests/input{i+1}.txt", "r")
    ##### 코드 짜기

    
    ##########
    print(f"최대공약수는: {gcd}")
    sys.stdin = open(f"tests/output{i+1}.txt", "r")
    output_list = list(map(int, input().split()))
    if gcd == output_list[0]:
        print("정답")
    else:
        print("뭔가가 잘못된듯")


