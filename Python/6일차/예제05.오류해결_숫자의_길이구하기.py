# number = 22020718 오류
number = str(22020718)
print(len(number))
# number의 타입이 int일 경우 len 함수 사용 불가 -> 자료형을 str로 변경해줘야함

# Traceback (most recent call last):
#   File "/Users/nahkim/Desktop/TIL/Python/6일차/예제05.오류해결_숫자의_길이구하기.py", line 7, in <module>
#     print(len(number))
# TypeError: object of type 'int' has no len()