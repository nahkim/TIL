word = input()

res = ''
for i in range(len(word)):
    if (word[i] != 'a'):
        res += word[i]

print(res)

# 방법 2
# res = ''
# for char in word:
#     if (char != 'a'):
#         res += char

# print(res)