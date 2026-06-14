class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = dict()
        for i in s:
            if i not in counter.keys():
                counter[i] = 1
            else:
                counter[i] = counter[i] + 1
        for j in t:
            if j not in counter.keys():
                return False
            else:
                counter[j] = counter[j] - 1
        for k in counter.keys():
            if counter[k] != 0:
                return False
        return True