class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hash map
        sdict = {}
        tdict = {}
        # sdict {'t': 1}

        for i in s:
            sdict[i] = 1 + sdict.get(i, 0)
        for j in t:
            tdict[j] = 1 + tdict.get(j, 0)

        return sdict == tdict
        # return sorted(s) == sorted(t) # O(nlogn)--> time complexity

