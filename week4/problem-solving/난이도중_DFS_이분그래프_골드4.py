# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707
"""
문제
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

예제 입력 1 
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
예제 출력 1 
YES
NO


아이디어
모든 정점에 대해 방문 여부 및 색상(예: 1 또는 -1)을 기록.
연결된 정점을 탐색하며 현재 정점과 다른 색으로 칠함.
이미 방문한 정점의 색이 현재 정점의 색과 같다면 이분 그래프가 아님. 
"""

import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]


    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)


    visited = [False] * len(graph)  # 방문 여부
    color = [0] * (v+1)     # 색칠
    
    def bfs(graph, start, visited, color):
        queue = deque()
        queue.append(start)
        visited[start] = True
        color[start] = 1

        while queue:
            x = queue.popleft()
            for i in graph[x]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    # 현재 노드 x와 반대 색으로 칠하기
                    color[i] = -color[x]
                else:
                    # 값이 같다면 이분 그래프가 아님
                    if color[i] == color[x]:
                        return True
                    
        return False

    #  그래프가 연결 그래프가 아닐 수 있으므로 모든 노드를 확인해야 함
    result = "YES"
    for i in range(1, v+1):
        if not visited[i]:
            # 같은 값을 발견했다면 true를 리턴해서 result = NO 가 됨
            if bfs(graph, i, visited, color):
                result = "NO"
                break

    print(result)