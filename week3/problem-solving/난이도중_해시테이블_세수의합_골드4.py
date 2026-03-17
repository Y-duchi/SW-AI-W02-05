# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295
# 입력
# 5
# 2
# 3
# 5
# 10
# 18
# 출력
# 18

"""
x + y = k - z

모든 (x + y) 값을 해시 테이블에 저장

모든 (k, z)에 대해
k - z가 해시에 있는지 확인

가장 큰 k 찾기

"""
import sys
input = sys.stdin.readline
n = int(input())
data = [int(input().strip()) for _ in range(n)]
data.sort()

def add_three_number():
    # 중복을 허용하지 않는 set
    s = set()

    # x + y의 모든 경우의 수를 중복 없이 set에 담기
    for i in range(n):
        for j in range(n):
            s.add(data[i]+data[j])


    for i in range(n-1, -1, -1):     # 큰 값부터 검사해서 s에 존재하면 바로 리턴
        for j in range(n):
            if data[i] - data[j] in s:
                return data[i]

print(add_three_number())
