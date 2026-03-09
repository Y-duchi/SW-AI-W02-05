# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예제 입력 1 
# 3
# 29
# 38
# 12
# 57
# 74
# 40
# 85
# 61
# 예제 출력 1 
# 85
# 8
# 1. 아이디어
#   1. 입력된 값들을 배열에 담는다. 
#   2. 배열안에서 max값을 찾는다
#   3. max 값과 일치하는 배열의 요소를 찾아 인덱스출력

import sys
input = sys.stdin.readline

def max_num():
    data = [int(input()) for _ in range(9)]
    max_num = max(data)
    print(max_num)
    for num in data:
        if num == max_num:
            print(data.index(num)+1)

max_num()