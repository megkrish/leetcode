"""
Leetcode top interview 150
https://leetcode.com/studyplan/top-interview-150/

Problem links:
1. https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
2. https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
3. https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
4. https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
5. https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # TODO: this is not the right solution work on it later
        del nums1[-(m - n):]
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        st = 0
        ed = len(nums) - 1
        while st <= ed:
            if nums[st] == val:
                # nums.append(nums.pop(st))
                nums.pop(st)
                ed -= 1
            else:
                st += 1
        return len(nums)

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st = 0
        ed = st + 1
        while ed < len(nums):
            if nums[st] == nums[ed]:
                nums.pop(ed)
            else:
                st = ed
                ed += 1
        return len(nums)

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        #TODO complete this solution ans is not correct
        """
        st = 0
        ed = st + 1
        count = 1
        while ed < len(nums):
            print(count)
            if nums[st] != nums[ed]:
                count = 1
            if nums[st] == nums[ed]:
                count += 1
                if count > 2:
                    nums.pop(ed)
                ed += 1
            else:
                st = ed
                ed += 1
        print(nums)

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 0

        return max(d, key=d.get)


s = Solution()
# s.merge([1, 2, 3, 0, 0, 0], 6, [2, 5, 6], 3)
# s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
# s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
# s.removeDuplicates2([0, 0, 1, 1, 1, 1, 2, 3, 3])
s.majorityElement([1, 2, 2, 1, 1, 1, 1, 2, 2])
