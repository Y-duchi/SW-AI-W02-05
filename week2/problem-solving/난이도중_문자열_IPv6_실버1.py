# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107
# 예제 입력 1 
# 25:09:1985:aa:091:4846:374:bb
# 예제 출력 1 
# 0025:0009:1985:00aa:0091:4846:0374:00bb


# 예제 입력 2 5개의 0000이 더 추가됨
# ::1
# 0000:0000:0000:0000:0000:0000:0000:0001
# 예제 출력 2 
# 0000:0000:0000:0000:0000:0000:0000:0001


# 23:34::12:21
# ::1
# 1::
# 1. 4개 씩 끊어 나타낸다. 
# 2. 앞자리의 0 전체 혹은 일부 생략 가능
# 3. 0으로만 이루어진 그룹이 있다면 : 만 남김
# 4. 총 길이는 8*4 = 32


def function(ip):
    if "::" in ip:  
        ip = ip.split("::") #[23:34], [12:21]
        left = ip[0].split(":") # [23,34]
        right = ip[1].split(":") # [12,21]

        left_block = []
        right_block = []

        for i in left:
            left_block.append(i.zfill(4)) #[0023, 0034]
        for i in right:    
            right_block.append(i.zfill(4))    # [0012, 0021]

        total = 8 - (len(left_block)+len(right_block))
        for _ in range(total):
            left_block.append("0000")
        ip = left_block + right_block
    else:
        ip = ip.split(":")
        for i in range(len(ip)):
            ip[i] = ip[i].zfill(4)
    
    print(":".join(ip))
  

ip = input()
function(ip)