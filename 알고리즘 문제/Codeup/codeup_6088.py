a, d, n = map(int, input().split())

res = a
for i in range(a, n + a - 1):
    res += d
print(res)

# 방법 2
# res = a
# i = 0
# while i < n - 1:
#     res += d
#     i += 1
# print(res)