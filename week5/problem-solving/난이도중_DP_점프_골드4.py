# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253
"""
문제
N(2 ≤ N ≤ 10,000)개의 돌들이 같은 간격으로 놓여 있다. 편의상 순서대로 1, 2, …, N번 돌이라고 부르자. 당신은 현재 1번 돌 위에 있는데, 이 돌들 사이에서 점프를 하면서 N번째 돌로 이동을 하려 한다. 이때 다음 조건들이 만족되어야 한다.

이동은 앞으로만 할 수 있다. 즉, 돌 번호가 증가하는 순서대로만 할 수 있다.
제일 처음에 점프를 할 때에는 한 칸밖에 점프하지 못한다. 즉, 1번 돌에서 2번 돌이 있는 곳으로 점프할 수 있다. 그 다음부터는 가속/감속 점프를 할 수 있는데, 이전에 x칸 점프를 했다면, 다음번에는 속도를 줄여 x-1칸 점프하거나, x칸 점프하거나, 속도를 붙여 x+1칸 점프를 할 수 있다. 물론 점프를 할 때에는 한 칸 이상씩 해야 한다.
각 돌들은 각기 그 크기가 다르고, 그 중 몇 개의 돌은 크기가 너무 작기 때문에 당신은 그러한 돌에는 올라갈 수 없다.
위와 같은 조건들을 만족하면서 1번 돌에서 N번 돌까지 점프를 해 갈 때, 필요한 최소의 점프 횟수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 두 정수 N, M(0 ≤ M ≤ N-2)이 주어진다. M은 크기가 맞지 않는, 즉 크기가 작은 돌의 개수이다. 다음 M개의 줄에는 크기가 작은 돌들의 번호가 주어진다. 1번 돌과 N번 돌은 충분히 크기가 크다고 가정한다.

출력
첫째 줄에 필요한 최소의 점프 횟수를 출력한다. 만약 N번 돌까지 점프해갈 수 없는 경우에는 -1을 출력한다.

예제 입력 1 
19 3
11
6
16
예제 출력 1 
6

아이디어
1. 작은 돌 set에 저장
2. 2번 돌이 막혀 있으면 -1
3. visited[돌][점프거리] 생성
4. queue = (2, 1, 1) 시작

5. BFS:
   while queue:
       현재 상태 꺼냄

       if N 도착 → 종료

       다음 점프 3개 생성:
           x-1, x, x+1

           조건 체크:
               - 1 이상
               - 범위 안
               - 작은 돌 아님
               - 방문 안 했음

           queue에 추가

6. 끝까지 못 가면 -1
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
s = set()
max_jump = int((2 * n) ** 0.5) + 2
visited = [[False] * (max_jump + 1) for _ in range(n + 1)]

for _ in range(m):
    mini_rock = int(input())
    s.add(mini_rock)

# 첫 점프는 무조건 1칸임, 2가 작은돌이면 못뜀
if 2 in s:
    print(-1)
    sys.exit()
    
queue = deque()
queue.append((2,1,1))   # 현재 돌, 직전 점프거리, 점프횟수
visited[2][1] = True

while queue:
    stone, jump, cnt = queue.popleft()

    # 목표도달: 현재 돌이 n까지 갔다면 최소 점프횟수 찾음
    if stone == n:
        print(cnt)
        sys.exit()

    for next_jump in (jump-1, jump, jump+1):
        if next_jump < 1:
            continue

        # 다음 도착 돌
        next_stone = stone + next_jump      

        # 작은 돌 만남
        if next_stone in s:
            continue

        # 범위 밖
        if next_stone > n:
            continue

        # 방문한 적 있으면 스킵
        if visited[next_stone][next_jump]:
            continue

        visited[next_stone][next_jump] = True
        queue.append((next_stone, next_jump, cnt+1))
print(-1)