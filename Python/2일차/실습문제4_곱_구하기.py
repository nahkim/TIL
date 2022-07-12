n = int(input())
res = 1
for i in range(1, n + 1):
    res *= i
print(res)


n = int(input())
i = 1
res = 1
while i <= n:
    res *= i
    i += 1
print(res)