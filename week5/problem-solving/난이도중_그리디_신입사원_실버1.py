# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946
"""
입력
첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다. 각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다. 두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다고 가정한다.

출력
각 테스트 케이스에 대해서 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원수를 한 줄에 하나씩 출력한다.

예제 입력 1 
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
예제 출력 1 
4
3

"""



import sys
input= sys.stdin.readline
t = int(input())


for i in range(t):
    n = int(input())
    result = []     # 선발된 사람들을 저장
    arr = []        # (서류, 면접) 저장 리스트
    for i in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))

    arr.sort()
    # 1 4는 서류 1등이므로 무조건 뽑힘
    result.append(arr[0])

    # 비교
    for i in range(1, len(arr)):
        # result[-1][1] = 지금까지 뽑힌 사람 중 최소 면접 순위
        # arr[i][1] = 현재 사람의 면접 순위
        # 현재 사람이 더 면접을 잘 봤다면
        if result[-1][1] > arr[i][1]:
            result.append(arr[i])       # 선발 명단에 추가


    print(len(result))