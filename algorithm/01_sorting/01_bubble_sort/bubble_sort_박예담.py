def bubble_sort(num):
    n = len(num)

    for i in range(n) :
        for j in range(0,n-i-1):
            if num[j] > num[j+1] : 
                new = num[j] 
                num[j] = num[j+1]
                num[j+1] = new 

        return num


num1 = [1,3 ,5 ,4, 2]
print("num1의 output : ", bubble_sort(num1))

num2 = [1, 4, 1, 2, 3]
print("num2의 output : ", bubble_sort(num2))
