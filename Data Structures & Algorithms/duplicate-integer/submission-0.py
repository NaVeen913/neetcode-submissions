class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uset = set()

        for i in range(len(nums)):
            if nums[i] in uset:
                return True
            else:
                uset.add(nums[i])
        return False