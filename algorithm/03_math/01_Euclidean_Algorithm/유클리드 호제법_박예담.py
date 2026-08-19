import sys

#실행코드
# 표준 입력을 키보드가 아닌 'data.txt' 파일로 변경
for i in range(4):
    sys.stdin = open(f"algorithm/03_math/01_Euclidean_Algorithm/tests1/input{i+1}.txt", "r")
    ##### 코드 짜기
    num_list = list(map(int,input().split()))
    max_num = max(num_list)
    min_num = min(num_list)
    gcd = 0 
    

    while min_num != 0 : 
        max_num, min_num = min_num, max_num % min_num 

    gcd = max_num
    
    ##########
    print(f"최대공약수는: {gcd}")
    sys.stdin = open(f"algorithm/03_math/01_Euclidean_Algorithm/tests1/output{i+1}.txt", "r")
    output_list = list(map(int, input().split()))
    if gcd == output_list[0]:
        print("정답")
    else:
        print("뭔가가 잘못된듯")
