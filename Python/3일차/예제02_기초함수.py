def rectangle(a, b):
    return a*b, (a + b) * 2

a, b = map(int, input().split())

print(rectangle(a, b))