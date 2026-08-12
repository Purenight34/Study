for i in range(4):
    sys.stdin = open(f"tests/input{i+1}.txt", "r")

    number_list = list(map(int, input().split()))
    big_number = max(number_list)
    small_number = min(number_list)
    remainder = 1
    gcd = 0
    while remainder > 0:
        if small_number > big_number:
            remainder = small_number % big_number
            small_number = remainder
            gcd = big_number
        elif big_number > small_number:
            remainder = big_number % small_number
            big_number = remainder
            gcd = small_number
        else:
            remainder = 0
            gcd = big_number

    print(f"최대공약수는: {gcd}")
    sys.stdin = open(f"tests/output{i+1}.txt", "r")
    output_list = list(map(int, input().split()))
    if gcd == output_list[0]:
        print("정답")
    else:
        print("뭔가가 잘못된듯")
