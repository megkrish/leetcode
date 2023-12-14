"""
Leetcode top interview 150
https://leetcode.com/studyplan/top-interview-150/

Problem links:
6. https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
7. https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)  # this is to avoid
        return nums[-k:] + nums[:-k]

    def buy_the_stock(self, bought, bought_day, buy, day):
        if buy < bought:
            bought = buy
            bought_day = day
        return bought, bought_day

    def sell_the_stock(self, sold, sell):
        if sell > sold:
            sold = sell
        return sold

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # TODO: this is not the right solution work on it later
        day = 1
        sold = prices[-1]
        bought = prices[0]
        bought_day = 0
        while day < len(prices):
            bought, bought_day = self.buy_the_stock(bought, bought_day,
                                                    prices[day], day)
            day += 1
        while bought_day < len(prices):
            sold = self.sell_the_stock(sold, prices[bought_day])
            bought_day += 1
        return sold - bought

    def jumped_to(self, now_at, nums):
        print(f"returning {nums[now_at]}")
        return nums[now_at]

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # TODO: this is not the right solution work on it later
        # i = 0
        # if len(nums) == 1 and nums[0] == 0:
        #     return True
        #
        # while i <= len(nums):
        #     if i == nums[-1]:
        #         return True
        #     print(i)
        #     i += self.jumped_to(i, nums)
        # else:
        #     return False

        start = 0
        end = start + nums[start]

        while True:
            end = self.jumped_to(start, end)
            start = end


s = Solution()
# print(s.rotate([1, 2], 3))
# print(s.maxProfit([2, 4, 1]))
print(s.canJump([3, 2, 1, 0, 4]))
# [2,3,1,1,4]
