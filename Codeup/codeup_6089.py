a, r, n = map(int, input().split())

# res = a
# for i in range(1, n):
#     res *= r
# print(res)

# 방법 2
res = a
i = 0
while i < n - 1:
    res *= r
    i += 1
print(res)