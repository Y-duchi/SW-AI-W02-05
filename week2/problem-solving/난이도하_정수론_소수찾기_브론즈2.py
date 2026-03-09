# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 예제 입력 1 
# 4
# 1 2, 3 6 7

# - 1은 소수가 아님
# - 2부터 자기 자신하고만 나누어 떨어지는 수
#    2부터 자기 자신 전까지 나누었을 때 나누어떨어진다면 소수가 아님
# - while n % 2부터 자신전까지 == 0: 
#       return 소수
        # 1을 뺴버려
#   소수 아님

import sys
input = sys.stdin.readline

def sosu():
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    
    for i in arr:
        if i == 1:
            continue
        p = True
        for j in range(2, i):
            if i % j == 0:
                p = False
                break

        if p:
            count += 1
    
    print(count)
    
sosu()