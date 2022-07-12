# 1부터 사용자가 입력한 양의 정수까지의 총합을 구하는 코드를 작성하시오

num = int(input())

sum = 0
i = 0
while i <= num:
    sum += i
    i += 1
print(sum)