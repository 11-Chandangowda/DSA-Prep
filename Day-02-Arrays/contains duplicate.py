def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


# test cases
print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))