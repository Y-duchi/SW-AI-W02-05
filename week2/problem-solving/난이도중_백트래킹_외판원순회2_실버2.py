# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971
# 4
# 0 10 15 20
# 5 0 9 10
# 6 13 0 12
# 8 8 9 0


n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

# 방문 여부
visited = [False] * n
# 최소 비용을 저장할 변수 (처음에는 아주 큰 값)
answer = float('inf')

def dfs(start, current, count, cost):
    global answer

    # 최소비용보다 현재비용이 더 커졌다면 볼 필요 없음
    if cost >= answer:
        return

    # 모든 도시 방문
    if count == n:
        # 현재 도시에서 출발 도시로 돌아갈 수 있는지
        if w[current][start] != 0:
            # 최소값 갱신
            answer = min(answer, cost + w[current][start])
        return

    for next_city in range(n):
        if not visited[next_city] and w[current][next_city] != 0:
            visited[next_city] = True
            dfs(start, next_city, count + 1, cost + w[current][next_city])
            visited[next_city] = False

visited[0] = True
dfs(0, 0, 1, 0)

print(answer)
