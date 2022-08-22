# shift 연산
# 지정한 비트수 만큼 밀어주는 연산 (<<, >>)
# n << k 일 경우 n * 2^k
# n >> k 일 경우 n * 1/2^k

n, m = map(int, input().split())
print(n << m)