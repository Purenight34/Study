def factorial(num) :
    if num ==0 or num== 1 : 
        return 1 
    return num * factorial(num-1)

def num_input() : 
    num = int(input())
    Number_Factorial = factorial(num)
    print(Number_Factorial)

num_input()