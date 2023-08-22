
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a,b,c,ans = nums[0],nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            a = nums[i]*a # 이전 최대값 *자기 자신
            b = nums[i]*b # 이전최소값 * 자기 자신
            c = nums[i] # 자기자신
            a,b = max(a,b,c),min(a,b,c)
            ans = max(ans,a)
        return ans