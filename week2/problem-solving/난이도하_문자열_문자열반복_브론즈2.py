# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
# 예제 입력 1 
# 2
# 3 ABC
# 5 /HTP

# 예제 출력 1 
# AAABBBCCC
# /////HHHHHTTTTTPPPPP

import sys
input = sys.stdin.readline

t = int(input()) # 입력받을 테스트 케이스 수

# 처음 푼 방식
def sentense(t):
    for _ in range(t):
        P = []
        r, s = input().split()
        r = int(r)

        for st in s:
            P.append(st * r)
        
        print(''.join(P))

# 두 번째 방식
def sentense(t):
    for _ in range(t):
        r, s = input().split()
        r = int(r)
        P = [st*r for st in s]
        
        print(''.join(P))


sentense(t)