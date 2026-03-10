# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

# 첫째 줄에 옮긴 횟수 K를 출력한다.
# N이 20 이하인 입력에 대해서는 두 번째 줄부터 수행 과정을 출력한다. 
# 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데,
# 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다. N이 20보다 큰 경우에는 과정은 출력할 필요가 없다.

n = int(input())
# 3

def function(n):
    print(2**n-1)
    def hanoi_tour(n, one, two, three):
        if n == 1:
            print(one, three)
            return
        
        hanoi_tour(n-1, one, three ,two )
        print(one, three)
        hanoi_tour(n-1, two, one, three)

    if n <= 20:
        hanoi_tour(n, 1, 2, 3)



function(n)