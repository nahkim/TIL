number = int(input())

cnt = 0
while number > 10:
    number = number / 10
    cnt += 1
cnt += 1
print(cnt)

# 다른 방법 문자열로 형변환
# print(len(str(number)))

# 조금 정석느낌
# result = 0

# while number != 0:            # while number:
#     number = number // 10         # number //= 10
#     result += 1
# print(result)