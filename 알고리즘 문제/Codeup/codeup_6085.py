w, h, b = map(int, input().split())

print(format(w * h * b / 8 / 1024 / 1024, ".2f"), "MB")
# round를 할경우 100 100 4일경우 소수점 한자리수 밖에 안나오는데 그 이유는?
# 왜 format형식만 되는가?

# 소수점 자리를 지정하는 4가지 방법
# round() : return float
# f-string : 문자열 형식
# "{}".format() : 문자열 형식
# format() : 문자열 형식