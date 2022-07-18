number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
# count += 1 들여쓰기를 하지 않아 for문이 끝나고서 한번 count 됨
    count += 1


print(format(total / float(count), ".1f"))