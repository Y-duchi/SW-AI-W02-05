# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470
# 출력
# 첫째 줄에 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 출력한다. 
# 출력해야 하는 두 용액은 특성값의 오름차순으로 출력한다. 특성값이 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우에는 그 중 아무것이나 하나를 출력한다.
# 예제 입력 1 
# 5
# -2 4 -99 -1 98
# 예제 출력 1 
# -99 98

"""
 -2 4 -99 -1 98
 -99 -2 -1 4 98

 

"""

def binary(data):
    data.sort()
    best = 9000000000 

    for i in range(0, n-1):
        target = -data[i]
        left = i + 1
        right = n - 1

        # 이분탐색
        while left <= right:
            mid = (left + right) // 2
            if data[mid] < target:
                # target보다 크거나 같은 값 중 가장 작은 값 4
                left = mid + 1
            else:
                # target보다 작은 값 중 가장 큰 값 -1
                right = mid -1
        # left가 배열 범위를 벗어나지 않았는지
        if left < n:
            left_sum = abs(data[i] + data[left]) 
            if left_sum < best:
                best = left_sum
                a = data[i]
                b = data[left]

        # 같은 원소를 두 번 사용하는 것을 막기 위한 조건
        if right > i:
            right_sum = abs(data[i] + data[right]) 
            if right_sum < best:
                best = right_sum
                a = data[i]
                b = data[right]
    
    print(a, b)


n = int(input())
# map: 문자열 리스트를 정수형 리스트로 변환해줌
data = list(map(int, input().split()))

binary(data)
