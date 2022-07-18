number = int(input())

cnt = 0
while number > 10:
    number = number / 10
    cnt += 1
cnt += 1
print(cnt)