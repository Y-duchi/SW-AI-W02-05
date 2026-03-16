# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630
# 첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.

# 8
# 1 1 0 0 0 0 1 1
# 1 1 0 0 0 0 1 1
# 0 0 0 0 1 1 0 0
# 0 0 0 0 1 1 0 0
# 1 0 0 0 1 1 1 1
# 0 1 0 0 1 1 1 1
# 0 0 1 1 1 1 1 1
# 0 0 1 1 1 1 1 1

# 출력
# 9
# 7

"""
크기가 N x N인 종이에 대해:
현재 구역이 전부 0인지, 전부 1인지 확인
전부 같으면
0이면 흰색 개수 +1
1이면 파란색 개수 +1
전부 같지 않으면
왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
이렇게 4개로 분할
각 구역에 대해 같은 작업 반복
"""

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0

def divide(x, y, size):
    global white, blue
    # 검사 시작점
    color = m[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if m[i][j] != color: 
                mid = size // 2
                divide(x, y, mid)    # 왼쪽위
                divide(x, y+mid, mid)    # 오른쪽 위
                divide(x+mid, y, mid)    # 왼쪽 아래
                divide(x+mid, y+mid, mid)    # 오른쪽 아래
                return
            
    if color == 0:
        white += 1
    else:
        blue += 1
   

divide(0,0,n)
print(white)
print(blue)