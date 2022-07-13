n = int(input())

sum = 0
count = 0
for i in range(1, n + 1):
    sum += i
    count += 1
    if (n <= sum):
        break
print(count)