class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        match = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in match:
                return [match[diff], i]
            match[n] = i
        