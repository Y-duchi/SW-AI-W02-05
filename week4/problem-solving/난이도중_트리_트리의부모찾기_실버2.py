# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
"""
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
예제 입력 1 
7
1 6
6 3
3 5
4 1
2 4
4 7
예제 출력 1 
4
6
1
3
1
4
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
"""
[
[],
[6, 4],
[4],
[5. 6],
[1,7.2],
[3],
[3,1]
[4]
]
"""
parent = [0] * (n+1) # [0,0,0,0,0,0,0,0]
visited = [False] * len(graph)
# [f,t,f,f,f,f,f]
def find_tree_parent(graph, start, visited, parent):

    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            parent[i] = start
            find_tree_parent(graph, i, visited, parent)


find_tree_parent(graph, 1, visited, parent)

for i in range(2, len(parent)):
    print(parent[i])