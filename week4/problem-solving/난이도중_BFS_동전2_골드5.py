# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294
"""
예제 입력 1 
3 15
1
5
12
예제 출력 1 
3

아이디어
sort정렬을 통해 큰 값부터 탐색하도록하기
타겟이 되는 모든 경우의 수를 bfs 
타겟이되면 몇개 썼는지 배열에 저장 그리고 거기서 min값 구하기


BFS는 이렇게 흘러가야 해:

시작: (0, 0)
→ 금액 0, 동전 0개
하나 꺼냄
모든 동전 더해봄
k 도착하면 종료

"""
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())    # 동전 종류, 타겟금액

coins = [int(input().strip()) for _ in range(n)]  



def bfs(total, count):
    queue = deque()
    queue.append((total, count))    # (현재금액, 동전 개수)
    visited = [False] * (k+1)       # 최소동전으로 만든적이 있는지 검사

    while queue :
        c, cnt = queue.popleft()
        
        for i in coins:
            total = i + c   # 현재금액 + 코인
            # 현재금액이 목표금액보다 커지면 안 찾음
            if total > k:
                continue 
            # 현재금액과 목표금액이 같다면 동전개수 +1 
            if total == k:
                return cnt + 1 
            
            # 방문하지 않았다면 방문처리하고, 큐에 현재금액이랑 동전개수 + 1 삽입
            if not visited[total]:
                visited[total] = True
                queue.append((total, cnt + 1))
            
    return -1
            
print(bfs(0,0))