# from pprint import pprint
# import sys

# sys.stdin = open('input.txt', 'r')
n = int(input())

list_ = [list(map(int, input().split())) for _ in range(n)]
# print(list_)
res = [[0] * 19 for _ in range(19)]
# print(res)
for i, j in list_:
    res[i - 1][j - 1] = 1
# pprint(res)
for i in range(19):
    for j in range(19):
        print(res[i][j], end=' ')
    print()