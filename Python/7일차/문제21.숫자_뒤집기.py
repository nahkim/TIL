num = int(input())

num_list = []
while num != 0:
    num_list.append(num % 10)
    num = num // 10

res = 0
num_len = len(num_list)
for i in range(len(num_list)):
    res += (10**i * num_list[num_len - i - 1])
print(res)

# 방법 2
# res = 0
# while num:
#     res *= 10
#     res += num % 10
#     num //= 10
# print(res)