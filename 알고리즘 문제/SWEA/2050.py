#import sys
#sys.stdin = open("input.txt", "r")

T = str(input())

for i in range(0, len(T)):
    if (ord(T[i]) >= 97):
        print(ord(T[i]) - 96, end=' ')
    else:
        print(ord(T[i]) - 64, end=' ')