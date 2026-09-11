"""스택을 이용한 DFS로 시작점에서 도착점까지 이동 가능한지 판단한다.

풀이
1. 단방향 통로를 인접 리스트에 저장한다.
2. 시작점을 스택에 넣고 visited에 방문 표시를 한다.
3. 스택에서 정점을 꺼내고, 미방문 이웃을 넣으면서 즉시 방문 표시한다.
   순환이 있어도 같은 정점은 스택에 한 번만 들어간다.
4. 탐색이 끝나면 도착점의 방문 여부로 '가능' 또는 '불가능'을 출력한다.

입력: T, 각 케이스의 N M, 간선 M개, 시작점 S와 도착점 E.
케이스마다 그래프와 visited를 새로 만든다.
시간 복잡도는 O(N + M), 그래프를 포함한 공간 복잡도는 O(N + M)이다.
"""

import sys


def dfs(graph, start):
    visited = [False] * len(graph)
    stack = [start]
    visited[start] = True

    while stack:
        current = stack.pop()

        for next_vertex in graph[current]:
            if not visited[next_vertex]:
                stack.append(next_vertex)
                # 넣을 때 표시해야 다른 경로에서 같은 정점을 또 넣지 않는다.
                visited[next_vertex] = True

    return visited


def main():
    test_case = int(input())

    for tc in range(test_case):
        n, m = map(int, input().split())
        graph = [[] for _ in range(n + 1)]

        for i in range(m):
            A, B = map(int, input().split()) 
            graph[A].append(B) #A에서 B로 향하는 경로

        start, end = map(int, input().split())
        visited = dfs(graph, start)

        # 시작점도 방문 표시했으므로 start == end이면 항상 '가능'이다.
        print("가능" if visited[end] else "불가능")


if __name__ == "__main__":
    main()
