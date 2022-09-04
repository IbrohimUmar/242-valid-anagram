from collections import Counter
class Solution2:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
