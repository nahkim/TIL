T = int(input())

for test_case in range(1, T + 1):
    word = input()
    res = 0
    if word == word[::-1]:
        print('#', test_case, ' ', 1, sep='')
    else:
        print('#', test_case, ' ', 0, sep='')