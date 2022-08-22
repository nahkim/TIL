n1, n2, n3 = input().split()

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

print ((n1 if (n1 < n2) else n2) if ((n1 if (n1 < n2) else n2) < n3) else n3)

# 어떤 순서에 따라 게산될지 생각해보기!