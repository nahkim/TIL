a, m ,d, n = map(int, input().split())

sum = a
for i in range(a, n + a - 1):
    sum = sum * m + d
print(sum)