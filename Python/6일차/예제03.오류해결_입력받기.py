numbers = input().split()
numbers = list(map(int, numbers))
# number의 자료형이 str이므로 sum함수를 사용하면 error -> number의 자료형을 int로 바꿔줌
print(sum(numbers))

# Traceback (most recent call last):
#   File "/Users/nahkim/Desktop/TIL/Python/6일차/예제03.오류해결_입력받기.py", line 4, in <module>
#     print(sum(numbers))
# TypeError: unsupported operand type(s) for +: 'int' and 'str'