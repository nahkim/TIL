num = int(input())
nums = input().split()

numlist = []
for i in range(num):
    nums[i] = int(nums[i])

for i in range(num - 1, -1, -1):
    print(nums[i], end=' ')