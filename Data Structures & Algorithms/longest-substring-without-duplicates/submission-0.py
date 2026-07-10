class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        uq= set()
        i = 0
        j = 0
        maxlen = 0
        for j in range(len(s)):
            while s[j] in uq:
                uq.remove(s[i])
                i += 1
            uq.add(s[j])
            maxlen = max(maxlen, j-i+1)
        return maxlen
