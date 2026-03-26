# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056
"""
입력
첫째 줄에 N이 주어진다.

두 번째 줄부터 N+1번째 줄까지 N개의 줄이 주어진다. 2번째 줄은 1번 작업, 3번째 줄은 2번 작업, ..., N+1번째 줄은 N번 작업을 각각 나타낸다. 각 줄의 처음에는, 해당 작업에 걸리는 시간이 먼저 주어지고, 그 다음에 그 작업에 대해 선행 관계에 있는 작업들의 개수(0 ≤ 개수 ≤ 100)가 주어진다. 그리고 선행 관계에 있는 작업들의 번호가 주어진다.

출력
첫째 줄에 모든 작업을 완료하기 위한 최소 시간을 출력한다.

예제 입력 1 
7
5 0
1 1 1
3 1 2
6 1 1
1 2 2 4
8 2 2 4
4 3 3 5 6
예제 출력 1 
23
힌트
1번 작업 : 0~5 
2번 작업 : 5~6
3번 작업 : 6~9 
4번 작업 : 5~11
5번 작업 : 11~12
6번 작업 : 11~19
7번 작업 : 19~23

"""
import sys
from collections import deque
input = sys.stdin.readline   # 빠른 입력 사용

n = int(input())  # 작업 개수
data = [list(map(int, input().split())) for _ in range(n)]  
# 입력 원본 저장 (각 줄: [시간, 개수, 선행작업들...])

def topological(data):
    graph = [[] for _ in range(n + 1)]  
    # 위상정렬용 그래프
    # graph[a] = [b, c] → a가 끝나야 b, c 가능

    indegree = [0] * (n + 1)  
    # 각 작업의 진입차수 (선행 작업 개수)

    time = [0] * (n + 1)  
    # 각 작업의 소요 시간

    result = [0] * (n + 1)  
    # 각 작업의 최소 완료 시간

    # --------------------------
    # 입력을 위상정렬 구조로 변환
    # --------------------------
    for i, work in enumerate(data):
        current = i + 1   # 작업 번호 (1부터 시작)

        time[current] = work[0]  
        # 현재 작업 시간 저장

        indegree[current] = work[1]  
        # 현재 작업의 선행 작업 개수

        for pre in work[2:]:  
            # 선행 작업 번호들 순회
            graph[pre].append(current)  
            # pre → current 간선 생성
            # 즉, pre가 끝나야 current 가능

    queue = deque()

    # --------------------------
    # 시작 작업 찾기 (진입차수 0)
    # --------------------------
    for i in range(1, n + 1):
        if indegree[i] == 0:  
            # 선행 작업 없는 작업
            queue.append(i)  
            # 바로 시작 가능

            result[i] = time[i]  
            # 시작시간 0 → 완료시간 = 자기 시간

    # --------------------------
    # 위상정렬 시작
    # --------------------------
    while queue:
        x = queue.popleft()  
        # 현재 작업 꺼냄 (이미 완료시간 확정된 작업)

        for nxt in graph[x]:  
            # x가 끝나면 할 수 있는 다음 작업들

            indegree[nxt] -= 1  
            # x가 끝났으므로 선행 작업 하나 해결

            # 핵심: 최소 완료 시간 갱신
            result[nxt] = max(result[nxt], result[x] + time[nxt])
            # 여러 선행 작업 중
            # 가장 늦게 끝나는 작업 기준으로 시작해야 함
                     
            if indegree[nxt] == 0:  
                # 모든 선행 작업 완료됨
                queue.append(nxt)  
                # 이제 실행 가능

    return max(result)  
    # 모든 작업 완료 시간 중 최댓값 = 전체 최소 완료 시간


print(topological(data))