# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())
    A = p * w
    B = q

    if (r <= w):
        B = q + s * (w - r)
    print('#', test_case, sep='', end=' ')
    if (A < B):
        print(A)
    else:
        print(B)