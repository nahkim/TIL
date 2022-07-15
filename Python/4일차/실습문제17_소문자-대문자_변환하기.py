word = input()

for i in range(len(word)):
    if (ord(word[i]) >= 97 and ord(word[i]) <= 122):
        print(chr(ord(word[i]) - 32), end='')