n = int(input())
arr = list(map(int, input().split()))

min = arr[n - 1]
for i in range(n - 1, -1, -1):
    if (arr[i] < min):
        min = arr[i]
print(min)