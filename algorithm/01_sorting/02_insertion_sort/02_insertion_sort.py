import sys

for i in range(3):
    sys.stdin = open(f"algorithm/01_sorting/02_insertion_sort/tests/input_0{i+1}.txt", "r")
    insertion_sort = list(map(int, input().split()))

    ######### 여기서부터 작성 
    n = len(insertion_sort)

    for j in range(1, n) : 
        for k in range(j,0,-1) : 
            if insertion_sort[k] < insertion_sort[k-1]  :
                insertion_sort[k],insertion_sort[k-1] = insertion_sort[k-1],insertion_sort[k]
            else : break 
    
    
    ##########
    print(f"삽입정렬 후 : {insertion_sort}")
    sys.stdin = open(f"algorithm/01_sorting/02_insertion_sort/tests/output_0{i+1}.txt", "r")
    output_list = list(map(int,input().split()))
    if insertion_sort == output_list : 
        print(f"Test{i+1} : 정답")
    else:
        print(f"Test{i+1} : 땡 틀렸습니다~")
