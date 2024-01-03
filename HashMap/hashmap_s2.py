"""
Leetcode top interview 150
https://leetcode.com/studyplan/top-interview-150/

Problem links:
1. https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150
2. https://leetcode.com/problems/happy-number/description/?envType=study
-plan-v2&envId=top-interview-150
3. https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150
4. https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        # TODO: Work on this
        """
        pass

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        # TODO: work on this
        """
        pass

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        #TODO: Solution exhausted time limit Work on it
        """
        slow = 0
        fast = 1
        if len(nums) <= 1:
            return False

        for i in range(len(nums) - 1):
            nxt = i + 1
            while nxt < len(nums):
                if nums[i] == nums[nxt] and abs(i - nxt) <= k:
                    return True
                nxt += 1
        return False

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # TODO: Invalid solution work on it 
        """
        cons = {}
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                print(nums[i], nums[j])
                diff = abs(nums[i] - nums[j])
                if diff not in cons:
                    cons[diff] = {nums[i], nums[j]}
                else:
                    cons[diff].update({nums[i], nums[j]})
        print(cons)
        return len(max(cons.values(), key=len))


so = Solution()
# print(so.twoSum([3, 2, 4], 6))
# print(so.isHappy(19))
# print(so.containsNearbyDuplicate([1, 0, 1, 1], 2))
# print(so.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(so.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
