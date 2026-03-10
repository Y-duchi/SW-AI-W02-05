# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819
# 예제 입력 1 
# 6
# 20 1 15 8 4 10
# 예제 출력 1 
# 62

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
list1 = list(map(int, input().split()))

def function(n, list1):
    result = [list(p) for p in permutations(list1, n)]
    answer = []
    for i in range(0, len(result)):
        max_number = 0
        for j in range(0, n-1):
            max_number += abs(result[i][j] - result[i][j+1])
        answer.append(max_number)


    print(max(answer))

function(n, list1)