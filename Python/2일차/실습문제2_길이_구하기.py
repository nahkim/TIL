# 1. while
word = 'happy!'
res = 0
while(res < len(word)):
    res += 1
print(res)

# 2. for (문자열 그대로)
word = 'happy!'

count = 0
for i in word:
    count += 1
print(count)

# 3. for (index)
word = 'happy!'

res = 0
for c in range(1, len(word) + 1):
    res += 1
print(res)