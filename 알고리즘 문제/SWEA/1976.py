T = int(input())

for test_case in range(1, T + 1):
    hour = 0
    minute = 0
    timer = list(map(int, input().split()))
    hour = timer[0] + timer[2]
    minute = timer[1] + timer[3]
    if hour > 12:
        hour -= 12
    if minute > 60:
        hour += 1
        minute -= 60
    print('#', test_case, ' ', hour, ' ', minute, sep='')
