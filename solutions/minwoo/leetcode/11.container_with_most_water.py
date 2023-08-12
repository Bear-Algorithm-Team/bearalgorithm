class Solution:
    def maxArea(self, height: List[int]) -> int: 

        ll = 0 
        rr = len(height)-1
        answer = 0
        while ll != rr :
            l_height = height[ll]
            r_height = height[rr]
            
            answer = max(answer, min(l_height,r_height)* (rr-ll))
            if l_height >= r_height :
                rr-=1
            else:
                ll+=1
        return answer
        