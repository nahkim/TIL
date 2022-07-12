# 사용자가 입력한 문자를 한글자씩 세로로 출력
chars = input()

for char in chars:
    print(char)

# 방법 2
# i를 기준으로 순회를 함
chars = input()
for i in range(len(chars)):
    print(chars[i])