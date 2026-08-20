def is_sorted(arr):
    # 배열이 오름차순으로 정렬되어 있는지 확인
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, comparisons


# 입력
arr = list(map(int, input().split()))
K = int(input())

# 정렬 여부 검사 후 이진 탐색 실행
if not is_sorted(arr):
    print("없음")
    print(0)  # 정렬이 안 되어 이진 탐색을 수행하지 않았으므로 비교 횟수는 0
else:
    index, comparisons = binary_search(arr, K)

    # 출력
    if index != -1:
        print(index)
    else:
        print("없음")

    print(comparisons)