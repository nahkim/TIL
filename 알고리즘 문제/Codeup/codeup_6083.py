num = list(map(int, input().split()))

cnt = 0

for i in range(num[0]):
    for j in range(num[1]):
        for k in range(num[2]):
            print(i, j, k)
            cnt += 1
print(cnt)