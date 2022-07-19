# 알맞은 기호 출력

# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n1, n2 = map(int, input().split())
    if n1 > n2:
        res = '>'
    elif n1 < n2:
        res = '<'
    else:
        res = '='

    print("#", test_case, sep='', end=' ')
    print(res)
