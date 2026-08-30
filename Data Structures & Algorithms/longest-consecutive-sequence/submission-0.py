class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        num_set = set(nums)
        max_len = 0

        for num in num_set:
            if num-1 not in num_set:
                curr = num
                len = 1

                while curr + 1 in num_set:
                    curr += 1
                    len += 1
                
                max_len = max(max_len, len)
        
        return max_len




        