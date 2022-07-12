# 1. while
word = 'happy!'
count = 0
while(count < len(word)):
    count += 1
print(count)

# 2. for (문자열 그대로)
word = 'happy!'
count = 0
for char in word:
    count += 1
print(count)

# 3. for (index)
word = 'happy!'
count = 0
for c in range(1, len(word) + 1):
    count += 1
print(count)