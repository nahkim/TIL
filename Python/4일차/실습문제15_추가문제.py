word = input()

res = []
for i in range(len(word)):
    if (word[i] == 'a'):
        res.append(i)
for i in range(len(res)):
    print(res[i], end=' ')