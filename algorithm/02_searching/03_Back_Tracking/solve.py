yedam = []

def Fist_of_the_North_Star(start, remaining) :
    if(remaining == 0) :
        if((yedam[0] == 1) and (yedam[-1] == 1)) :
            return
        print(''.join(map(str, yedam)))
        return
        
    for i in range(start, len(yedam)) :
        yedam[i] = 1
        Fist_of_the_North_Star(i + 1, remaining - 1)
        yedam[i] = 0
    return

n, m = map(int, input().split())
for i in range(n) : 
    yedam.append(0)
Fist_of_the_North_Star(0, m)