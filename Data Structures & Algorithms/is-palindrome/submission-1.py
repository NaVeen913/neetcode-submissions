class Solution:
    def isPalindrome(self, s: str) -> bool:
        sp = ""

        for i in s:
            if ord('A') <= ord(i) <= ord('Z') or ord('a') <= ord(i) <= ord('z') or ord('0') <= ord(i) <= ord('9'):
                sp += i.lower()


        i = 0
        j = len(sp) - 1

        while i < j:
            if sp[i] == sp[j]:
                i += 1
                j -= 1
            else:
                return False
        return True        