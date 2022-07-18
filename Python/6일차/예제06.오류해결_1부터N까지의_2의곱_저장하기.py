N = 10
# answer = ()   #오류
# 출력값이 리스트이므로 []로 변경해줘야한다. 또한 tuple은 append 사용 불가
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)


# Traceback (most recent call last):
#   File "/Users/nahkim/Desktop/TIL/Python/6일차/예제06.오류해결_1부터N까지의_2의곱_저장하기.py", line 6, in <module>
#     answer.append(number * 2)
# AttributeError: 'tuple' object has no attribute 'append'