# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
"""
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

예제 입력 1 
7
6
1 2
2 3
1 5
5 2
5 6
4 7

아이디어
1. 그래프 생성 
    graph = [0: [], 1: []]
2. 큐 사용
    큐를 이용해 bfs탐색 후 인접노드 result 에 담기
3. 결과 1도 배열에 들어가기 때문에
    return len(result) - 1

"""

"""
[[],
[2,5],
[3],
[],
[7],
[2,6]
]
"""

import sys
from collections import deque
n = int(input())
e = int(input())
graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
  
visited = [False] * len(graph)


def bfs(graph, start, visited):
    result = []
    queue = deque([start])
    visited[start] = True

    while queue:
        x = queue.popleft()
        result.append(x)
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return len(result) - 1



print(bfs(graph, 1, visited))