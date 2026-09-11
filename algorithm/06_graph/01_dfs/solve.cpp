#include <iostream>
#include <stack>
#include <vector>

using namespace std;

/*
풀이
1. 단방향 통로 u -> v를 인접 리스트 graph[u]에 저장한다.
2. 시작점을 스택에 넣고 방문 표시한 뒤, 스택이 빌 때까지 탐색한다.
3. 현재 정점에서 이동할 수 있는 미방문 정점을 스택에 넣고 즉시 표시한다.
   visited는 순환과 여러 경로로 인한 중복 삽입을 막는다.
4. 탐색이 끝난 뒤 visited[E]가 true이면 "가능", 아니면 "불가능"이다.
   시작점을 처음부터 표시하므로 S와 E가 같아도 "가능"이다.

각 테스트 케이스마다 그래프, 방문 배열, 스택을 새로 만든다.
한 케이스의 시간 복잡도: O(N + M)
한 케이스의 공간 복잡도: O(N + M), 그래프를 제외한 추가 공간은 O(N)
*/

vector<bool> dfs(const vector<vector<int>>& graph, int start) {
    // 방 번호가 1부터 N까지이므로 0번 칸은 사용하지 않는다.
    vector<bool> visited(graph.size(), false);
    stack<int> st;

    st.push(start);
    visited[start] = true;

    while (!st.empty()) {
        int current = st.top();
        st.pop();

        // 이웃을 입력 순서대로 넣으면 마지막에 넣은 정점부터 탐색한다.
        for (int next : graph[current]) {
            if (!visited[next]) {
                st.push(next);
                // 꺼낼 때까지 기다리지 않고 넣는 즉시 방문 표시한다.
                visited[next] = true;
            }
        }
    }

    return visited;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (!(cin >> T)) {
        return 0;
    }

    for (int tc = 0; tc < T; ++tc) {
        int N, M;
        cin >> N >> M;
        vector<vector<int>> graph(N + 1);

        for (int i = 0; i < M; ++i) {
            int u, v;
            cin >> u >> v;
            graph[u].push_back(v);  // 단방향이므로 u -> v만 저장한다.
        }

        // M개 통로를 모두 읽은 다음 줄이 시작점과 도착점이다.
        int S, E;
        cin >> S >> E;

        vector<bool> visited = dfs(graph, S);
        cout << (visited[E] ? "가능" : "불가능") << '\n';
    }

    return 0;
}
