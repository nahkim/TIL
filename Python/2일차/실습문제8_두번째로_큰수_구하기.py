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