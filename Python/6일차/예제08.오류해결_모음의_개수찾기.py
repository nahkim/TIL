word = "HappyHacking"

count = 0

for char in word:
    # if char == "a" or "e" or "i" or "o" or "u":
    # char == e가 아니라 e 자체를 보기 때문에 char에 무엇이 들어와도 참이 된다
    if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u") == True:
        count += 1

print(count)