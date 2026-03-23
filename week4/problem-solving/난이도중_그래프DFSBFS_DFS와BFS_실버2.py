# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260
"""
출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1 
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1 
1 2 4 3
1 2 3 4
예제 입력 2 
노드, 간선, 루트
5 5 3
5 4
5 2
1 2
3 4
3 1
예제 출력 2 
3 1 2 5 4
3 1 4 2 5


"""



import sys
input = sys.stdin.readline
from collections import deque

def dfs(graph, start, visited):
    result = [start]
    visited[start] = True

    # 정렬된 값으로 작은 값부터 우선탐색
    for i in sorted(graph[start]):
        if not visited[i]:
            result.extend(dfs(graph, i, visited))

    return result

def bfs(graph, start):
    result = []
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        x = queue.popleft()
        result.append(x)
        for i in sorted(graph[x]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return result



n, e, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
dfs_visited = [False] * len(graph)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs_result = dfs(graph, start, dfs_visited)
bfs_result = bfs(graph, start)

print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))