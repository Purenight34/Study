### 상단 - 담당자와 설명
담당 : 박은하

재귀함수란? -> 함수 안에서 자기 자신을 다시 호출하는 함수
계속 자신을 호출하게 되므로, 무한하게 반복되지 않도록 종료 조건이 필요하다.

반복문 없이 재귀함수를 사용해 팩토리얼을 계산하는 문제다.

입력은 0이상의 정수 Number가 주어진다.
출력은 양의 정수 Number!을 계산하여 출력한다.

### 중단 - 의사코드

팩토리얼 함수(int Number) 
  if Number이 0이거나 1
    return 1
  return Number * 팩토리얼(Number-1)
팩토리얼 함수 끝

메인 함수
  Number 입력
  Number_Factorial = 팩토리얼 함수(Number)
  Number_Factorial 출력
메인 함수 끝

### 하단
input_01 일반적인 정수 값이 입력된다.
input_02, 03에는 경계값이 입력된다.
input_04는 큰 값이 입력된다.