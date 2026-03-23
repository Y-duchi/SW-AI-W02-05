# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639
"""
입력
트리를 전위 순회한 결과가 주어진다. 노드에 들어있는 키의 값은 106보다 작은 양의 정수이다. 모든 값은 한 줄에 하나씩 주어지며, 노드의 수는 10,000개 이하이다. 같은 키를 가지는 노드는 없다.

출력
입력으로 주어진 이진 검색 트리를 후위 순회한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1 
50
30
24
5
28
45
98
52
60
예제 출력 1 
5
28
24
45
30
60
52
98
50

전위 순회 결과는 50 30 24 5 28 45 98 52 60 이고, 후위 순회 결과는 5 28 24 45 30 60 52 98 50

아이디어
현재 구간의 첫 값이 루트
그 다음 루트보다 처음 큰 값 찾기 (mid)
구간 나누기
왼쪽: start+1 ~ mid-1
오른쪽: mid ~ end
재귀:
왼쪽
오른쪽
마지막에 루트 출력
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


data = []
while True:
    x = input().strip()
    if x == "":
        break
    data.append(int(x))

def postorder(start, end):
    if start > end:
        return

    root = data[start]
    mid = end + 1

    for i in range(start + 1, end + 1):
        if data[i] > root:
            mid = i
            break

    postorder(start + 1, mid - 1)   # 왼쪽
    postorder(mid, end)             # 오른쪽
    print(root)                     # 루트

postorder(0, len(data) - 1)