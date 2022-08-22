number = int(input())
res = 0

while number != 0:  # while number:
    res += number % 10
    number //= 10

    # 방법 2
    # number, remainder = divmod(number, 10)
    # res += remainder
print(res)