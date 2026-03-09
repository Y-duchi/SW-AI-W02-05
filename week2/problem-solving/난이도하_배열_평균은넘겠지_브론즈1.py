# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344
# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91

# 5개의 테스트 케이스를 입력받음
# 5는 입력받을 학생들의 점수 개수
# 학생들의 점수 평균을 냄 : 350/5 = 70
# 배열에서 70점을 넘는 학생을 찾아 백분율 : 2/5 % 100 = 40
# 소수점 넷째 자리에서 반올림
import sys
input = sys.stdin.readline

t = int(input())

def average():
    for _ in range(t):
        data = list(map(int, input().split()))
        n = data[0]  # 5
        scores = data[1:] #50 50 70 80 100
        cnt = 0

        avg = sum(scores) / n
        for score in scores:
            if score > avg:
                cnt += 1
        per = cnt / n * 100
        print(f"{per:.3f}%")


average()