import sys
sys.stdin = open("노드_input.txt")

T = int(input())

def BFS():
    global distance
    front = 0       # 현 깊이에서 갈 수 있는 곳 중 몇 개 탐색했냐
    distance += 1   # 현 깊이에서 갈 수 있는곳 거리(출발 지점에서 갈 수 있는 곳은 거리 1)
    Queue_number = len(Queue)      # 현 지점에서 탐색 가능한 수
    while front < Queue_number:     # 탐색가능한 곳 다 탐색할 때 까지
        front += 1  # 탐색 시작했으니 하나 탐색함 +1
        current = Queue.pop(0)      # 현재 어디지?
        for i in V_info[current]:       # 현재 위치에서 갈 수 있는 곳을 방문했다고 기록하고 다음에 갈 곳에 저장
            if visited[i] == 0:
                visited[i] = 1
                Queue.append(i)
        if visited[G] == 1:     # 목표 지점 탐색 했으면 BFS 끝
            break
    else:       # 목표지점 탐색 못했어
        if Queue_number != 0:   # 탐색할 곳이 있으면 한 번 더 탐사 ㄱㄱ
            BFS()
        else:
            distance = 0    # 탐색 다 했는데 목표지점 탐색 못했네? 없어




for test_case in range(1, T+1):
    V, E = map(int, input().split())    # V: 노드 개수, E: 간선 정보 개수
    V_info = [[] for _ in range(V+1)]   # 간선 정보 담는 리스트
    for i in range(E):      # 간선 정보 담기(양방향)
        s, e = map(int, input().split())   
        V_info[s].append(e)
        V_info[e].append(s)
    S, G = map(int, input().split())    # S: 시작 지점, G: 목적 지점
    visited = [0] * (V+1)   # 방문 기록 생성
    Queue = []      # 큐 생성
    visited[S] = 1  # 시작 지점은 방문 했으니 방문 기록
    Queue.append(S)     # 큐에 출발 지점 투입
    distance = 0    # 출발 지점은 출발 지점에서 0이니깐 0으로 기록
    BFS()   # 탐색 시~작


    print(f"#{test_case} {distance}")

