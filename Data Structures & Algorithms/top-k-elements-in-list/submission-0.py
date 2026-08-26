class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        grp = {}
        for num in nums:
            key = num
            if key not in grp:
                grp[key] = 1
            else:
                grp[key] += 1
        
        sorted_items = sorted(grp.items(), key = lambda x : x[1], reverse = True)

        res = []
        for i in range(k):
            res.append(sorted_items[i][0])
        
        return res
        