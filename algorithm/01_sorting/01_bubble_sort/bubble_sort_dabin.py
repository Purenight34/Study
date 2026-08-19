#    n = 배열의 길이를 변수 n에 할당한다.

#    for i in 전체 배열 순회
#        for j in 배열의 끝에서 정렬된 부분을 제외하고 남은 부분을 순회
#            if arr[j]가 arr[j + 1]보다 크다면
#                arr[j]와 arr[j + 1]의 위치를 교환 
#    정렬된 값 arr 반환
# 메인 함수 끝
# 1 4 1 2 3
numbers = list(map(int, input().split()))
arr_len = len(numbers)

for i in range(arr_len):
    for j in range(arr_len-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j+1], numbers[j] = numbers[j], numbers[j+1] 

print(numbers)