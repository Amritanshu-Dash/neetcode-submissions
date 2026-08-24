from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count1 : dict[str, int] = defaultdict(int)
        for i in s:
            count1[i] += 1

        count2 : dict[str, int] = defaultdict(int) 
        for j in t:
            count2[j] += 1

        return count1 == count2

        

        