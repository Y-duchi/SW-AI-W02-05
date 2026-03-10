# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.

# 출력
# 각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.


# 예제 입력 1 
# 3
# 8
# 10
# 16
# 예제 출력 1 
# 3 5
# 5 5
# 5 11

"""
1.아이디어
    소수를 먼저 판별한다. 
    소수라면 소수 내에서 순열을 만들어 data[i]값과 일치되는 것을 찾아서 배열에 저장
    만약 파티션이 여러개가 나온다면 두 소수의 차이가 가장 작은 것을 출력 
    출력은 작은것 큰것
    a를 하나 정함

b = n - a 계산

a, b가 둘 다 소수인지 확인

가운데부터 찾으면 처음 나온 쌍이 정답
"""

t = int(input())
data = [int(input()) for i in range(t)]


def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for i in data:
    divide = i // 2
    for n in range(divide, 1, -1):
        b = i - n
        if is_prime(b) and is_prime(n) :
            print (n, b)
            break




