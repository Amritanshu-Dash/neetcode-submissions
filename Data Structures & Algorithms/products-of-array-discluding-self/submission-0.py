class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        i, j = 0, len(nums) - 1

        prefix = []
        postfix = [0] * len(nums)

        pre_prod = 1
        post_prod = 1

        while(i < len(nums) and j >= 0):
            pre_prod *= nums[i]
            prefix.append(pre_prod)
            post_prod *= nums[j]
            postfix[j] = post_prod
            i+=1
            j-=1

        res = []
        res.append(postfix[1])

        for i in range(1, len(nums) - 1):
            res.append(prefix[i-1] * postfix[i+1])

        res.append(prefix[len(nums) - 2])

        return res