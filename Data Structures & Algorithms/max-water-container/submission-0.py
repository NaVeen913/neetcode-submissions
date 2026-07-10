class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        maxw = 0

        while i < j:
            minw = min(heights[i], heights[j])
            maxw = max(maxw, minw*(j - i))
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return maxw
        