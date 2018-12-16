# encoding:utf-8
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        end_index = -1
        i = 0
        while i < len(nums) + end_index:
            if nums[i] + nums[end_index] > target:
                end_index -= 1
            elif nums[i] + nums[end_index] == target:
                return [i, len(nums) + end_index]
            else:
                for j in range(end_index - 1, -len(nums) + i, -1):
                    if nums[i] + nums[j] == target:
                        return [i, len(nums) + j]
                i += 1

a = Solution()
nums = [3,2,4]
target = 7
print(a.twoSum(nums,target))