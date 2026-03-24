n = int(input())
nums = list(map(int, input().split()))
count = 0
k = 1
nums.sort()
for x in nums:
    if x >= k:
        count += 1
        k += 1
print(count)