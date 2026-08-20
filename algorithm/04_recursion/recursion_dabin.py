def multiply(number):
    if number <= 1:
         return 1
    return number * multiply(number-1)

n = int(input())
numbers = multiply(n)

print(numbers)