import os

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

# -------------------------------------------------------------
# 현재 merge_sort.py가 있는 위치
current_dir = os.path.dirname(os.path.abspath(__file__))

# tests 폴더 위치
test_dir = os.path.join(current_dir, "tests")


# TEST 01 ~ TEST 04 실행
for i in range(1, 5):

    input_path = os.path.join(
        test_dir,
        f"input_{i:02d}.txt"
    )

    output_path = os.path.join(
        test_dir,
        f"output_{i:02d}.txt"
    )

    # input 파일 읽기
    with open(input_path, "r", encoding="utf-8") as f:
        arr = list(map(int, f.read().split()))

    # output 정답 파일 읽기
    with open(output_path, "r", encoding="utf-8") as f:
        expected = f.read().strip()

    # 병합 정렬 실행
    result = merge_sort(arr)

    # 출력 형태로 변환
    actual = " ".join(map(str, result))

    # 정답 비교
    if actual == expected:
        print(f"TEST_{i:02d}: PASS")

    else:
        print(f"TEST_{i:02d}: FAIL")
        print(f"입력값 : {arr}")
        print(f"기대값 : {expected}")
        print(f"실제값 : {actual}")

    print("-" * 40)