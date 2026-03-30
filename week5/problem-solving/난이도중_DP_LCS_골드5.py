# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251
"""
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

예제 입력 1 
ACAYKP
CAPCAK
예제 출력 1 
4

"""

import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

dp = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]

# LCS 값 채워넣기
for i in range(len(str1)+1):
    for j in range(len(str2)+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        # 같은 문자열을 발견 했다면
        elif str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        # 같은 문자열 발견 못했다면
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
# LCS 문자열 역추적 (dp 테이블을 거꾸로 따라가기)
result = []
i = len(str1)
j = len(str2)
while i > 0 and j > 0:
   # 두 문자가 같다면 → LCS에 포함, 대각선 이동
    if str1[i-1] == str2[j-1]:
        result.append(str1[i-1])
        i -= 1
        j -= 1
    # 다르면 → 더 큰 값을 가진 방향으로 이동
    elif dp[i-1][j] >= dp[i][j-1]:
        i -= 1
    else:
        j -= 1


print(len(result))