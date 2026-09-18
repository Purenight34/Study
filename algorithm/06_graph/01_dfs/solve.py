"""의사코드에 따라 스택으로 탐색하고 도착점의 방문 여부를 판단한다.

풀이
1. 단방향 통로를 인접 리스트에 저장한다.
2. visited를 미방문(0)으로 준비하고, 시작점을 스택에 넣고 방문(1) 표시한다.
3. 스택이 빌 때까지 현재 정점을 하나씩 꺼낸다.
4. 현재 정점의 이웃을 하나씩 확인하고, 미방문이면 스택에 넣고 방문 표시한다.
5. 모든 탐색이 끝난 뒤 visited[도착점]이 1이면 '가능', 0이면 '불가능'이다.

입력: T, 각 케이스의 N M, 간선 M개, 시작점 S와 도착점 E.
케이스마다 그래프와 visited를 새로 만든다.
시간 복잡도는 O(N + M), 그래프를 포함한 공간 복잡도는 O(N + M)이다.
"""

def dfs(graph, start):
    visited = [0] * len(graph)

    # 빈 스택에 시작 정점을 넣고 방문(1)으로 표시한다.
    stack = []
    stack.append(start)
    visited[start] = 1

    while stack: # stack -> 내가 방문할 목록들이 있으면
        current = stack.pop() # 가장 위에 방문한거 

        # 현재 위치에 연결된 다음 위치들을 하나씩 확인한다.
        for next_vertex in graph[current]: #current에서 갈 수 있는 다른 칸들
            if visited[next_vertex] == 0: #안들렀으면
                stack.append(next_vertex) #방문 목록에 넣어놓고
                visited[next_vertex] = 1 # 방문 표시
    return visited


def main():
    test_case = int(input())

    for _ in range(test_case):
        n, m = map(int, input().split())
        graph = [[] for _ in range(n + 1)]

        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append(v)  # u에서 v로 향하는 단방향 통로

        start, end = map(int, input().split())
        visited = dfs(graph, start)

        # 시작점도 방문 표시했으므로 start == end이면 항상 '가능'이다.
        print("가능" if visited[end] == 1 else "불가능")


if __name__ == "__main__":
    main()
