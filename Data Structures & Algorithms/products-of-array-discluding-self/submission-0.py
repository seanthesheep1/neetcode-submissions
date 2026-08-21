class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Output = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            Output[i] = left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            Output[i] *= right
            right *= nums[i]

        return Output