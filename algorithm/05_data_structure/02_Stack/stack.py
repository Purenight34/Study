brackets = input()
temp_brackets = []

for bracket in brackets:
    if bracket == '(':
        temp_brackets.append(bracket)
    else:
        if len(temp_brackets) == 0:
            print('NO')
            break
        else:
            temp_brackets.pop()
else:
    if len(temp_brackets) == 0:
        print('YES')
    else:
        print('NO')