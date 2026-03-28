# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

"""
문제
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 
이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

예제 입력 1 
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
예제 출력 1 
4


"""

import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    a, b = map(int, input().split())
    data.append((a,b))
# 끝나는 시간 우선, 같으면 시작 시간 기준 정렬
data.sort(key=lambda x:(x[1], x[0]))
current = data[0][1]
# 처음 회의는(0번째) 선택이 되어있으므로 1로 시작
count = 1
for i in range(1, n):
    # 현재회의의 끝나는 시간보다 다음 회의의 시작 시작이 크다면 회의 가능
    if data[i][0] >= current:
        count += 1  # 회의 개수 증가
        current = data[i][1]    # 찾은 다음회의로 현재 회의 갱신

print(count)