### 상단 - 담당자와 설명
담당 : 박은하

동적 배열이란? 
동적 배열(Dynamic Array)의 구조와 동작을 이해하고 직접 구현한다.

고정 크기 배열과 달리 동적 배열은 저장 공간이 부족해지면
더 큰 배열을 새로 생성하고 기존 데이터를 복사하여 크기를 확장한다.

- 생성자
- 소멸자
- `pushBack(value)` : 배열의 마지막에 값을 추가한다.
- `pop()` : 배열의 마지막 값을 제거한다.
- `get(index)` : 지정한 위치의 값을 반환한다.
- `getSize()` : 현재 저장되어 있는 원소의 개수를 반환한다.

해당 Class를 구현하고, 명령어에 따라서 위 내부 함수를 실행하는 .exe 파일을 생성한다.

입력은 .exe 파일 실행 이후 아래 명령어와 인자를 입력하여 작동한다.
p(pushBack), o(pop), g(get), s(getSize), a(print all), q(quit(), 프로그램 종료)

출력은

### 중단 - 의사코드
```text
Class MyDynamicArray 선언

  <!-- class 변수 선언 -->
  data, 값
  size, 현재 크기
  capacity, 최대 크기(차지하는 메모리 양)


  생성자 
    size ← 0
    capacity ← 2

    capacity 크기의 배열을 생성한다.
    data가 생성한 배열의 메모리를 가리키도록 한다.

  소멸자
    data가 가리키고 있는 배열을 제거한다.

  함수 pushBack(value)
      If 현재 크기 == 최대 크기
          newCapacity ← capacity * 2
          newCapacity 크기의 새로운 배열 newData를 생성한다.

          For Data
              newData[i] ← data[i]로 데이터를 이전한다.

          기존 data 배열을 제거한다.
          기존 메모리를 가르키는 곳을 변경한다.
          클래스 변수에 새로운 값 newCapapcity와 newData를 할당한다.

      data[size]에 value 입력
      size += 1


  함수 pop()
    If size > 0
      size ← size - 1

  함수 get(index)

    IF index < 0 OR index >= size
      범위를 벗어나니, 오류 호출

    Return data[index]

  Function getSize()

    Return size

Class 끝

메인 함수 시작
  Class MyDynamicArray 생성
  While 종료 명령어 전까지
    order 입력받기
    switch order 
      만약 p라면
        value 입력받기
        pushBack(value) 실행
      만약 o라면
        pop 실행
      만약 g라면
        index 입력받기 
        배열[index] 출력
      만약 s라면
        배열 크기 출력
      만약 a라면
        배열 전부 출력
      만약 q라면
        프로그램 종료
```

### 하단
직접 exe 파일 제작 후 실행하여 확인한다.