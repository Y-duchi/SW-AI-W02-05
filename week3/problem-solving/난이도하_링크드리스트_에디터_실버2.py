# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

# L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
# 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $	$라는 문자를 커서 왼쪽에 추가함
# 예제 입력 1 
# abcd
# 3
# P x
# L
# P y
# 예제 출력 1 
# abcdyx

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor = None   # 커서의 왼쪽 노드

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # 노드를 추가하고 마지막 노드를 변경하는 코드
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def process_commands(self, commands):
        self.cursor = self.tail   # 처음 커서는 맨 뒤

        for cm in commands:
            # L: 커서를 왼쪽으로
            if cm[0] == "L":
                if self.cursor is not None:
                    self.cursor = self.cursor.prev

            # D: 커서를 오른쪽으로
            elif cm[0] == "D":
                if self.cursor is None:
                    self.cursor = self.head
                elif self.cursor.next is not None:
                    self.cursor = self.cursor.next

            # B: 커서 왼쪽 문자 삭제
            elif cm[0] == "B":
                if self.cursor is None:
                    continue

                node = self.cursor
                self.cursor = node.prev

                # 노드가 하나뿐인 경우
                if node == self.head and node == self.tail:
                    self.head = None
                    self.tail = None

                # 첫 노드 삭제
                elif node == self.head:
                    self.head = node.next
                    self.head.prev = None

                # 마지막 노드 삭제
                elif node == self.tail:
                    self.tail = node.prev
                    self.tail.next = None

                # 중간 노드 삭제
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev

            # P x: 커서 왼쪽에 x 추가
            elif cm[0] == "P":
                x = cm[1]
                new_node = Node(x)

                # 맨 앞에 삽입하는 경우
                if self.cursor is None:
                    new_node.next = self.head
                    if self.head is not None:
                        self.head.prev = new_node
                    self.head = new_node
                    if self.tail is None:
                        self.tail = new_node
                    self.cursor = new_node

                # 맨 뒤(현재 cursor가 tail) 뒤에 삽입
                elif self.cursor == self.tail:
                    self.tail.next = new_node
                    new_node.prev = self.tail
                    self.tail = new_node
                    self.cursor = new_node

                # 중간 삽입
                else:
                    next_node = self.cursor.next
                    self.cursor.next = new_node
                    new_node.prev = self.cursor
                    new_node.next = next_node
                    next_node.prev = new_node
                    self.cursor = new_node

    def get_string(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return ''.join(result)


linkedlist = LinkedList()

data = input().strip()
n = int(input())
command = [input().split() for _ in range(n)]

for ch in data:
    linkedlist.append(ch)

linkedlist.process_commands(command)
print(linkedlist.get_string())