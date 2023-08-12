class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        ans = 10**9+1
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans = min(ans,nums1[i])
                i+=1
                j+=1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                i+=1
        while i < len(nums1): # num1 이 남은경우
            if nums2[j-1] == nums1[i]:
                ans = min(ans,nums1[i])
            i+=1
        while j < len(nums2):
            if nums1[i-1] == nums2[j]:
                ans = min(ans, nums2[j])
            j+=1
        if ans == 10**9+1 :
            return -1
        return ans