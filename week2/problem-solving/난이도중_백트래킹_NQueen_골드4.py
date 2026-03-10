# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

"""
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)
출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다

1. 아이디어
    각 행에는 퀸 하나씩 => 행에서 퀸이 겹칠일 없음
    어느 열에 둘 지 정한다.
    열, \ , / 은 둘 수 없음

   
"""

# 시간 초과 ㅜㅜ
# n = int(input())          # 체스판 크기 입력
# count = 0                 # 가능한 배치 수
# queen = [0] * n           # queen[row] = col

# def Nqueen(row):            # row행에 퀸을 놓는 함수
#     global count

#     if row == n:          # 모든 행에 퀸을 다 놓았으면
#         count += 1        # 경우의 수 1 증가
#         return

#     for col in range(n):  # 현재 row행의 모든 열을 하나씩 시도
#         can_place = True  # 현재 위치에 퀸을 놓을 수 있다고 가정

#         for i in range(row):   # 이전 행들의 퀸과 충돌 검사
#             if queen[i] == col:   # 같은 열에 퀸이 있으면
#                 can_place = False # 놓을 수 없음
#                 break

#             if abs(row - i) == abs(col - queen[i]):  
#                 # 같은 대각선에 퀸이 있으면
#                 can_place = False # 놓을 수 없음
#                 break

#         if can_place:           # 이전 퀸들과 충돌하지 않는다면
#             queen[row] = col    # 현재 row행의 퀸을 col열에 놓기
#             Nqueen(row + 1)       # 다음 행으로 이동해서 재귀 탐색

# Nqueen(0)                         # 0행부터 탐색 시작
# print(count)                    # 가능한 전체 경우의 수 출력

n = int(input())          # 체스판 크기 입력
count = 0                 # 가능한 배치 수

col_used = [False] * n            # col_used[col] = 해당 열에 퀸이 있는지
diag1 = [False] * (2 * n - 1)     # \ 대각선 사용 여부 (row - col + n - 1)
diag2 = [False] * (2 * n - 1)     # / 대각선 사용 여부 (row + col)

def Nqueen(row):          # row행에 퀸을 놓는 함수
    global count

    if row == n:          # 모든 행에 퀸을 다 놓았으면
        count += 1        # 경우의 수 1 증가
        return

    for col in range(n):  # 현재 row행의 모든 열을 하나씩 시도
        d1 = row - col + n - 1   # \ 대각선 번호
        d2 = row + col           # / 대각선 번호

        if col_used[col] or diag1[d1] or diag2[d2]:
            continue

        col_used[col] = True
        diag1[d1] = True
        diag2[d2] = True

        Nqueen(row + 1)   # 다음 행으로 이동해서 재귀 탐색

        col_used[col] = False
        diag1[d1] = False
        diag2[d2] = False

Nqueen(0)                 # 0행부터 탐색 시작
print(count)              # 가능한 전체 경우의 수 출력