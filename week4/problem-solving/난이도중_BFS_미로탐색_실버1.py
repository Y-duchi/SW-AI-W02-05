# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178

"""
출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

예제 입력 1 
4 6
101111
101010
101011
111011
예제 출력 1 
15
예제 입력 2 
4 6
110110
110110
111111
111101
예제 출력 2 
9

아이디어
visited 배열은 해당 칸의방문여부

시작점 (0, 0)에서 출발
상하좌우로 이동
범위 밖이면 못 감
값이 0이면 못 감
아직 안 간 1인 칸만 감
그 칸의 거리는 현재 칸 거리 + 1
BFS니까 처음 도착한 값이 최단거리

"""

import sys
from collections import deque
input = sys.stdin.readline

rows, cols = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(rows)]

def bfs(row, col):
    visited = [[False] * cols for _ in range(rows)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((row, col))
    visited[row][col] = True

    
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            # 맵을 벗어나면
            if not (0 <= nx < rows and 0 <= ny < cols) :
                continue
            # 0이면
            if maze[nx][ny] == 0:
                continue
            # 이미 방문했으면
            if visited[nx][ny]:
                continue
            # 1 이면서 이미 방문도 안 했고 범위 안이라면
            visited[nx][ny] = True
            maze[nx][ny] = maze[r][c] + 1
      
            queue.append((nx, ny))


    return maze[rows - 1][cols - 1]


result = bfs(0,0)
print(result)