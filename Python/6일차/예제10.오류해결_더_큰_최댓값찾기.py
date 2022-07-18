number_list = [1, 23, 9, 6, 91, 59, 29]
# max = max(number_list)
# 예약 변수를 변수명으로 사용해서 오류 발생
max1 = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max1 > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max1 < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")


# Traceback (most recent call last):
#   File "/Users/nahkim/Desktop/TIL/Python/6일차/예제10.오류해결_더_큰_최댓값찾기.py", line 7, in <module>
#     max2 = max(number_list2)
# TypeError: 'int' object is not callable