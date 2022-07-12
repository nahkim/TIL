n = int(input())

if (n < 0 and n % 2 == 0):
    print("A")
elif (n < 0 and n % 2 == 1):
    print("B")
elif (n > 0 and n % 2 == 0):
    print("C")
elif (n > 0 and n % 2 == 1):
    print("D")

# 방법 2
# if (n < 0):
#     if (n % 2 == 0):
#         print('A')
#     else:
#         print('B')
# else:
#     if (n % 2 == 0):
#         print('C')
#     else:
#         print('D')