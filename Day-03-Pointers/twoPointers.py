print("START")

def twoPointer(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
    
    if current_sum == target:
        return True

    elif current_sum < target:
         left += 1

    else:
        right -=1

    return False


print(twoPointer([2,7,11,15], 9)) 
print(twoPointer([1,2,3,4], 8))