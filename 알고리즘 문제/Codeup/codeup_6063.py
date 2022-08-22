n1, n2 = input().split()

n1 = int(n1)
n2 = int(n2)

res = (n1 if (n1 > n2) else n2)
print(res)

# 3항 연산자
# 넣을 변수 = (참 일경우 if(조건) else 거짓일 경우))