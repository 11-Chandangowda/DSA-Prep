# Sliding Window (Fixed Size)

## 🧠 Concept
Sliding Window is used to reduce time complexity when working with subarrays.

Instead of recalculating the sum of every subarray:
- Reuse previous result
- Remove outgoing element
- Add incoming element

---

## 🎯 Problem
Find maximum sum of subarray of size k

Example:
nums = [1,3,2,6,-1,4,1,8,2]
k = 5

---

## 🪟 Key Idea

new_sum = old_sum - outgoing + incoming

---

## 🔄 Steps

1. Calculate first window sum:
   sum(nums[:k])

2. Set max_sum = current_sum

3. Slide window:
   - Remove element leaving window → nums[i-k]
   - Add new element → nums[i]

4. Update max:
   if current_sum > max_sum:
       max_sum = current_sum

---

## ⏱ Time Complexity
O(n)

## 💾 Space Complexity
O(1)

---

## 💻 Code

```python
def maxSumSubarray(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, len(nums)):
        current_sum = current_sum - nums[i-k] + nums[i]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum