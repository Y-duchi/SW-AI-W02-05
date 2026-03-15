# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933
# 예제 입력 1 
# 4
# las
# god
# psala
# sal
# 예제 출력 1 
# 3 a
# 예제 입력 2 
# 4
# kisik
# ptq
# tttrp
# tulipan
# 예제 출력 2 
# 5 s

"""
1. for 문을 돌며
    글자가 회문인지 확인
        맞다면 민균이 비밀번호 길이, 중간 단어 출력
        리턴
    글자가 이미 나온적이 있다면
        정답
    나온적이 없다면
        저장

리스트는 값을 찾을 때 앞에서부터 하나씩 비교(O(n))해야 하지만, 해시(set/dict)는 키의 해시값으로 바로 위치를 찾아 확인(O(1))하기 때문에 더 빠르다.
    
"""

n = int(input())
data = [input().strip() for _ in range(n)]
# ["las", "god", "pasla","sal"]

def password(data):
    dict = {}
    for word in data:
        if word[::-1] == word: 
            print(len(word), word[len(word) // 2])
            return
        elif word[::-1] in dict:
            print(len(word), word[len(word) // 2])
            return
        else:
            dict[word] = True
            

password(data)