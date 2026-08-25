"""
담당자: 권은준()
문제: Queue는 먼저 들어온 것을 먼저 내보내는(FIFO) 자료구조이다.
'입력'을 하면 값이 큐의 맨 뒤에 추가되고,
'출력'을 하면 큐의 맨 앞에 있는 값이 나온다.
"""
"""
제한조건
1. append, pop, insert, remove등 리스트의 삽입/삭제 메서드 사용 금지
2. collections.deque등 파이썬이 제공하는 큐 관련 자료구조 사용 금지
"""

def Queue_input(information):
    global last_index
    global numbers
    numbers[last_index] = information
    last_index += 1
    if last_index == len(numbers):
        Full_numbers()        


def Queue_output():
    global first_index
    global numbers
    print(f"출력한 수: {numbers[first_index]}")
    first_index += 1
    

def Full_numbers():
    global numbers
    global last_index
    global first_index
    New_numbers = [None] * int(len(numbers) * 1.25)
    New_number = first_index
    for number in range(last_index - first_index):
        New_numbers[number] = numbers[New_number]
        New_number += 1
        New_number %= len(numbers)
    last_index = last_index - first_index
    numbers = New_numbers
    first_index = 0

numbers = [None] * 5
first_index = 0
last_index = 0
while True:
    i = input("무엇을 할까요?") 
    if i == "입력":
        information = input("내용: ")
        Queue_input(information)
        print("추가 완료")
    elif i == "출력":
        if first_index == last_index:
            print("리스트가 비어있습니다.")
        else:
            Queue_output()
        
    else:
        break