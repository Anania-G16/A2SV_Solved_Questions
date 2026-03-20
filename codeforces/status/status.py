n, s = list(map(int, input().split()))
nums = list(map(int, input().split()))
 
left = 0
rsum = 0
count = 0
 
for right in range(n):
    rsum += nums[right]
    
    while rsum > s:
        rsum -= nums[left]
        left += 1
    
    count += right - left + 1
print(count)