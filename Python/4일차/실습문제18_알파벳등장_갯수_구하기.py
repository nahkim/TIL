word = input()

res = {}
for i in range(len(word)):
    if (word[i] in res):
        res[word[i]] += 1
    else:
        res[word[i]] = 1
for i in res:
    print(i, res.get(f'{i}'))