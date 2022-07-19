# 평균 구하기

T = int(input())
for test_case in range(1, T + 1):
    num = map(int, input().split())
    res = sum(num)

    print("#", test_case, sep='', end=' ')
    print(round(res / 10))