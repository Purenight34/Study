import sys
sys.stdin = open("미로_input.txt")

T = int(input())

def BFS():
    global distance
    distance += 1
    Queue_number = len(Queue_x) #   현재 깊이에서 방문해야할 횟수
    front = 0                   # 현재 깊이에서 방문한 횟수
    while Queue_number > front:    # 현재 깊이에서 방문한 횟수가 방문해야할 횟수랑 같기 전까지
        front += 1      # 방문 했으니 +1
        current_x = Queue_x.pop(0)
        current_y = Queue_y.pop(0)
        # 현재 위치에서 갈 수 있는 곳을 Queue에 넣기
        # 위
        if current_y - 1 >= 0:
            if miro[current_y - 1][current_x] == 0:
                Queue_x.append(current_x)
                Queue_y.append(current_y - 1)
                miro[current_y - 1][current_x] = 1  # 방문한 곳은 1로 표시
            elif miro[current_y - 1][current_x] == 3:
                miro[current_y - 1][current_x] = 1
                break
        # 아래
        if current_y + 1 < N:
            if miro[current_y + 1][current_x] == 0:
                Queue_x.append(current_x)
                Queue_y.append(current_y + 1)
                miro[current_y + 1][current_x] = 1
            elif miro[current_y + 1][current_x] == 3:
                miro[current_y + 1][current_x] = 1
                break
            # 왼쪽
        if current_x - 1 >= 0:
            if miro[current_y][current_x - 1] == 0:
                Queue_x.append(current_x - 1)
                Queue_y.append(current_y)
                miro[current_y][current_x - 1] = 1
            elif miro[current_y][current_x - 1] == 3:
                miro[current_y][current_x - 1] = 1
                break
        # 오른쪽
        if current_x + 1 < N:
            if miro[current_y][current_x + 1] == 0:
                Queue_x.append(current_x + 1)
                Queue_y.append(current_y)
                miro[current_y][current_x + 1] = 1
            elif miro[current_y][current_x + 1] == 3:
                miro[current_y][current_x + 1] = 1
                break


    else:
        if Queue_number != 0:   # 갈 곳이 있나?  -> 갈 곳이 없었으면 추가가 없음.
            BFS()





for test_case in range(1, T+1):
    N = int(input())    # 가로, 세로의 길이
    miro = [[] for _ in range(N)]
    for i in range(N):
        miro[i] = list(map(int, input()))
    distance = -1    # 출발 지점에서의 거리
    Queue_x = []  # 방문할 곳을 넣기
    Queue_y = []
    for y in range(N):
        for x in range(N):
            if miro[y][x] == 2:
                Queue_x.append(x)  # 스타트지점 방문예정 Queue에 넣기
                Queue_y.append(y)
    BFS()
    for y in range(N):
        for x in range(N):
            if miro[y][x] == 3:
                distance = 0

    print(f"#{test_case} {distance}")






