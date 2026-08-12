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


