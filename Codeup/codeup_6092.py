n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

d = []
for i in range(23):
    d.append(0)

for i in a:
    d[i - 1] += 1

for i in range(23):
    print(d[i], end=' ')