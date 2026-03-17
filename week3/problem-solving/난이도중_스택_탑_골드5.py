# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493
# 출력
# 첫째 줄에 주어진 탑들의 순서대로 각각의 탑들에서 발사한 레이저 신호를 수신한 탑들의 번호를 하나의 빈칸을 사이에 두고 출력한다. 만약 레이저 신호를 수신하는 탑이 존재하지 않으면 0을 출력한다.
# 예제 입력 1 
# 5
# 6 9 5 7 4
# 예제 출력 1 
# 0 0 2 2 4

# 0,6 

import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))

def top():
    stack = []       # (i, h)로 넣기
    result = []
    for i in range(n):
        # 스택이 비어있지 않으면서 and 마지막 스택의 높이 < 현재 데이터[i] 번째의 높이
        while stack and stack[-1][1] < data[i]:
            stack.pop()

        if not stack:
            result.append(0)
        else:
            result.append(stack[-1][0]+1)
        
        stack.append((i, data[i]))

    return result
        
  
    
print(top())