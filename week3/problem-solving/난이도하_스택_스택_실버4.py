# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 14
# push 1
# push 2
# top
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# top

# data = [["push", "1"], ["push", "2"], "top", "size"]
def function(data):

    stack = []

    for cm in data:
        if cm[0] == "push" :
            x = cm[1]
            stack.append(x)
        elif cm[0] == "pop":
            if len(stack) >= 1:
                x = stack.pop()
                print(x)
            else:
                print(-1)
        elif cm[0] == "size":
            print(len(stack))
        elif cm[0] == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif cm[0] == "top":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
            
                
       



n = int(input())
data = [input().split() for _ in range(n)]

function(data)