# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

# mississipi
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
# 알파벳을 딕셔너리에 넣기, 넣을 때마다 값 +1

def word():
    data = input()
    data = data.lower()

    result = {}

    for word in data:
        result[word] = result.get(word, 0) + 1
    
    max_value = max(result.values())
    if list(result.values()).count(max_value) > 1 : 
        return "?"
    else:
        for key, value in result.items():
            if value == max_value:
                return key.upper()

   
print(word())