def twoSum(nums, target):
    hashmap = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in hashmap:
            return [hashmap[complement], i]

        # FIXED: correct variable + correct indentation
        hashmap[nums[i]] = i


# test
nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))