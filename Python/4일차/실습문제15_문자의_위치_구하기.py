word = input()
check = 0
for i in range(len(word)):
    if (word[i] == 'a'):
        print (i)
        check = 1
        break
if (check == 0):
    print(-1)