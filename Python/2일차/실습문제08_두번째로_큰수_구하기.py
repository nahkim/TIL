numbers = [0, 20, 100]
# numbers = [0, 20, 100, 50, -60, 50, 100] # 50
# numbers = [0, 1, 0] # 0
# numbers = [-10, -100, -30] # -30

max = numbers[0]
min = numbers[0]

for i in numbers:
    if (max < i):
        max = i
    if (min > i):
        min = i

second_max = min
for i in numbers:
    if (i != max and second_max < i):
        second_max = i
print(second_max)

# 방법 2
# max_num = float("-inf")
# second_num = float("-inf")
# for n in numbers:
#     if max_num < n:
#         # 최대값이었던 것이 두번째로 큰수
#         second_num = max_num
#         max_num = n
#     elif second_num < n < max_num:  # elif second_num < n and n < max_num:
#         second_num = n
# print(second_num)