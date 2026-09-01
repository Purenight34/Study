import sys 
from collections import defaultdict 
from collections import deque

sys.stdin = open("tests/input.txt", 'r')

# n : 노드의 수 , m : 간선의 수 
n, m = map(int, input().split())

# 노드 연결 준비 
G = defaultdict(list)

# 노드 연결 
for _ in range(m):
    u, v = map(int, input().split())
    G[u].append(v)

# ////////////////////////////////////////////////////
def dfs(start):
    visited_order = []
    visited = [False] * (n + 1)
    
    stack = deque()
    stack.append(start)
    
    while stack: 
        v = stack.pop()
        
        if not visited[v]:
            visited[v] = True
            visited_order.append(v)
            
  
            for u in reversed(G[v]):
                if not visited[u]:
                    stack.append(u)
                    
    return visited_order
# //////////////////////////////////////////////////////
my_result = dfs(1) 


with open("tests/output.txt", 'r', encoding='utf-8') as f:
    expected_result = list(map(int, f.read().split()))

if my_result == expected_result:
    print(f"정답 : {my_result}")
else:
    print(f"오답 : {my_result} (기대값: {expected_result})")