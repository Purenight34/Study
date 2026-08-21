def linear_search(arr, k) :
    n = len(arr)

    for i in range(n) : 
        if arr[i] == k : 
            return i 

    return "없음"


n = int(input())
arr = list(map(int, input().split()))
K = int(input())

print(linear_search(arr, K))