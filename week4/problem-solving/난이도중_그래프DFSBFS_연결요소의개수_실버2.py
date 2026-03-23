# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724
"""
출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1 
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력 1 
2
예제 입력 2 
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
예제 출력 2 
1

따로 찾는 게 아니라 전체 정점을 순서대로 검사한다
즉:

for i in range(1, n+1)

아직 방문 안 했으면

그 i를 시작점으로 BFS 실행

BFS가 끝나면 그 덩어리 하나를 다 방문한 것

다음 미방문 정점을 만나면 또 새 BFS 시작
"""


import sys
input = sys.stdin.readline
from collections import deque

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 노드의 방문 여부 배열 선언
visited = [False] * len(graph)
count = 0

# bfs 탐색
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 전체 정점을 순서대로 검사
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        bfs(graph, i, visited)

print(count)