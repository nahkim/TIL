import sys

# sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    tmp = num
    mul = 1

    res = [0 for i in range(0, 10)]
    while sum(res) != 10:
        tmp = num * mul
        while tmp != 0:
            tmp, remainder = divmod(tmp, 10)
            res[remainder] = 1
        mul += 1
    print('#',test_case, sep='', end=' ')
    print(num * (mul - 1))  # 2번째 while문 끝나고 mul += 1이 되니 빼줘야함