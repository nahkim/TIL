#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
i = 1
for test_case in range(1, T + 2):
    print(i, end=' ')
    i *= 2
