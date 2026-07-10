class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difdict = {}

        for i, num in enumerate(nums):
            difdict[num] = i
            
        for i, n in enumerate(nums):
            diff = target - n
            if diff in difdict and difdict[diff]!= i:
                return [i, difdict[diff]]            
        