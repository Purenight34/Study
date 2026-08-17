"""
담당자: 권은준
- 문제
실수 n 개의 수가 입력으로 주어진다.(단, n은 20개가 넘지 않는다.)
들어온 정수를 오름차순으로 정렬하여 출력하는 문제이다.
"""

import os

base_dir = os.path.dirname(os.path.abspath(__file__))
test_dir = os.path.join(base_dir, "tests")

input_path = os.path.join(test_dir, "input.txt")
output_path = os.path.join(test_dir, "output.txt")

with open(input_path, "r", encoding="utf-8") as f:
    inputs = f.read().splitlines()

with open(output_path, "r", encoding="utf-8") as f:
    expected_outputs = f.read().splitlines()

for i, (inp, expected) in enumerate(zip(inputs, expected_outputs), start=1):
    numbers = list(map(float, inp.split()))

    # ============================================
    # 여기부터 알고리즘 구현 (직접 작성)
    #
    # [요구조건]
    # 1. sort(), sorted() 사용 금지
    # 2. 입력은 numbers로 고정되어 있음
    # 3. * sorted_numbers 에 오름차순으로 정렬된 결과를 담을 것 *
    #    (numbers를 직접 변형해도 되고, 새 리스트에 옮겨 담아도 됨)
    # 4. 반복문이 끝났을 때 sorted_numbers는
    #    numbers와 원소 구성은 같고 순서만 오름차순이어야 함
    # 5. sorted_numbers 리스트 내부 수들은 *실수*여야 함
    # ============================================



    # ============================================
    # 알고리즘 구현 끝
    # ============================================

    expected_nums = list(map(float, expected.split()))

    if sorted_numbers == expected_nums:
        print(f"{i}번째 줄: 정답 ✅")
    else:
        print(f"{i}번째 줄: 오답 ❌ (내 답: {sorted_numbers}, 정답: {expected_nums})")