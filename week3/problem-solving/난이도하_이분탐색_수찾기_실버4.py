# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
# 예제 입력 1 
# 5
# 정렬 4 1 5 2 3
# 5
# target 1 3 7 9 5
# 예제 출력 1 
# 1
# 1
# 0
# 0
# 1

"""
5
1 2 3 4 5
5
1 3 7 9 5

1 3 7 9 5 를 돌면서 이게 1 2 3 4 5 이분탐색하여 있다면 1 리턴 없으면 0 리턴
"""

def divide(arr, target_arr):
    arr.sort()

    for target in target_arr:
        tf = False
        left = 0
        right = len(arr)-1
        while left <= right :
            mid = (left + right) // 2
            if arr[mid] == target:
                tf = True
                print(1)
                break
            elif arr[mid] > target:
                right = mid -1
            else :
                left = mid+1
                

        if not tf:
            print(0)



n = int(input())
arr = list(map(int, input().split()))
m = int(input())
target_arr = list(map(int, input().split()))

divide(arr, target_arr)