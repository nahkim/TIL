numbers = [3, 10, 20]

avr = 0
for i in numbers:
    avr += i
print(int(avr / len(numbers)))

# 방법 2
result = 0
count = 0
for number in numbers:
    result += number
    count += 1
print(result/count)