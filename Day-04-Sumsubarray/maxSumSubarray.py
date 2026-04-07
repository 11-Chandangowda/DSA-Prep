def maxSumSubarray(nums, k):
    current_sum = sum(nums[:k])  #first window nums = [1,3,2,6,-1,...], k = 5
    max_sum = current_sum  #max = first window

    for i in range(k, len(nums)):     #i = 5 → next element after first window
        current_sum = current_sum - nums[i-k] + nums[i] #Core Sliding Formula

        if current_sum > max_sum:
            max_sum = current_sum #if bigger → update max

            return max_sum
print(maxSumSubarray([1,3,2,6,-1,4,1,8,2], 5))
