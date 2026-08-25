
def Queue_input(information):
    global last_index
    global numbers
    numbers[last_index] = information
    last_index += 1
    last_index %= len(numbers)
    if last_index == first_index:
        Full_numbers()        


def Queue_output():
    global first_index
    global numbers
    print(f"출력한 수: {numbers[first_index]}")
    numbers[first_index] = None
    first_index += 1
    first_index %= len(numbers)
    

def Full_numbers():
    global numbers
    global last_index
    global first_index
    New_numbers = [None] * int(len(numbers) * 1.25)
    New_number = first_index
    for number in range(len(numbers)):
        New_numbers[number] = numbers[New_number]
        New_number += 1
        New_number %= len(numbers)
    last_index = len(numbers)
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


