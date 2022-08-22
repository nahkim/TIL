#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    res = 1
    for i in range(2, num + 1):
        if (i % 2 == 0):
            res -= i
        else:
            res += i
    print("#", test_case, sep='', end=' ')
    print(res)
