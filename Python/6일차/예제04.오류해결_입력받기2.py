# words = list(map(int, input().split())) 오류
# words의 타입을 int로 할경우 오류 발생
words = list(input().split())
print(words)

# Traceback (most recent call last):
#   File "/Users/nahkim/Desktop/TIL/Python/6일차/예제04.오류해결_입력받기2.py", line 7, in <module>
#     words = list(map(int, input().split()))
# ValueError: invalid literal for int() with base 10: "I'm"