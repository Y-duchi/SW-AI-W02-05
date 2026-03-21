# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
"""
‘쩰리’는 가로와 세로의 칸 수가 같은 정사각형의 구역 내부에서만 움직일 수 있다. ‘쩰리’가 정사각형 구역의 외부로 나가는 경우엔 바닥으로 떨어져 즉시 게임에서 패배하게 된다.
‘쩰리’의 출발점은 항상 정사각형의 가장 왼쪽, 가장 위의 칸이다. 다른 출발점에서는 출발하지 않는다.
‘쩰리’가 이동 가능한 방향은 오른쪽과 아래 뿐이다. 위쪽과 왼쪽으로는 이동할 수 없다.
‘쩰리’가 가장 오른쪽, 가장 아래 칸에 도달하는 순간, 그 즉시 ‘쩰리’의 승리로 게임은 종료된다.
‘쩰리’가 한 번에 이동할 수 있는 칸의 수는, 현재 밟고 있는 칸에 쓰여 있는 수 만큼이다. 칸에 쓰여 있는 수 초과나 그 미만으로 이동할 수 없다.

출력
‘쩰리’가 끝 점에 도달할 수 있으면 “HaruHaru”(인용부호 없이), 도달할 수 없으면 “Hing” (인용부호 없이)을 한 줄에 출력합니다.
예제 입력 1 
3
1 1 10
1 5 1
2 2 -1
예제 출력 1 
HaruHaru
쩰리는 맨 왼쪽 위의 칸에서 출발해 (행, 열)로 나타낸 좌표계로,  (1, 1) -> (2, 1) -> (3, 1) -> (3, 3)으로 이동해 게임에서 승리할 수 있다.

예제 입력 2 
3
2 2 1
2 2 2
1 2 -1
예제 출력 2 
Hing
"""

## 런타임 에러
# import sys
# input = sys.stdin.readline
# n = int(input())
# # [[2,2,1],[2,2,2],[1,2,-1]]
# map = [list(map(int, input().split())) for _ in range(n)]

# def jumpking(row, col):

#     if 0 <= row < n and 0 <= col < n:
#         start = map[row][col]   # 2
#         # -1 찾으면 하루하루
#         if map[row][col] == -1:
#             return "HaruHaru"
#         # 아니면 탐색
#         right = jumpking(row, col + start)   # 오른쪽 이동
#         if right == "HaruHaru":
#             return "HaruHaru"
#         bottom = jumpking(row + start, col)    # 아래 이동
#         if bottom == "HaruHaru":
#             return "HaruHaru"
        
        
#         return "Hing"
    
#     if not (0 <= row < n and 0 <= col < n):
#         return "Hing"


# print(jumpking(0,0))

import sys
input = sys.stdin.readline
n = int(input())
# [[2,2,1],[2,2,2],[1,2,-1]]
map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def jumpking(row, col, visited):
    # 배열 범위 내 탐색
    if 0 <= row < n and 0 <= col < n:
        start = map[row][col]   # 2
       
        # -1 찾으면 하루하루
        if map[row][col] == -1:
            return "HaruHaru"
        # 이미 방문한 곳인지 확인
        if visited[row][col]:
            return "Hing"
        visited[row][col] = True
        # 아니면 탐색
        right = jumpking(row, col + start, visited)   # 오른쪽 이동
        if right == "HaruHaru":
            return "HaruHaru"
        bottom = jumpking(row + start, col, visited)    # 아래 이동
        if bottom == "HaruHaru":
            return "HaruHaru"
        
        return "Hing"
        
    else:
        return "Hing"


print(jumpking(0,0, visited))