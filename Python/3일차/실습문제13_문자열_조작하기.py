word = input()

res = ''
len = len(word) - 1
while len >= 0:
    res += word[len]
    len -= 1
print(res)

# 방법
for i in range(len(word)):
    print(word[len(word) -i - 1], end='')

# 방법 2
word = 'apple'
reseult = ''
for char in word:
    result = char + result  # 순서 중요
print(result)

# 방법 3
print(word[::-1])

# 방법 4
print(''.join(reversed(word)))
