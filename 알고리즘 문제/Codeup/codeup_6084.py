h, b, c, s = map(int, input().split())

res = 0
print(round(h * b * c * s /8 / 1024 / 1024, 1), 'MB')