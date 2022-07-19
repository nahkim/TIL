# 몫과 나머지 출력

T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    div, mod = divmod(a, b)
    print('#', test_case, sep='', end=' ')
    print(div, mod, sep=' ')