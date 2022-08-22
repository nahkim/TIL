c = ord(input())
a = ord('a')
while (a <= c):
    print(chr(a), end=' ')
    a += 1

# ord() : 알파벳 문자의 정수값 알아내는 함수
# chr() : 유니코드 문자로 변환