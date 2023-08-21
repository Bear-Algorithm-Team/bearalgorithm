class Solution:
    def longestPalindrome(self, s: str) -> str:        
        # 가운데부터 확장시켜 나간다. 펠린드롬이면 저장한다. 
        max_len = 0
        ans_ll = 0 
        ans_rr = 0

        for i in range(len(s)):
            ll = i
            rr = i 
            # 홀수길이(center 문자가 1개) 문자열 탐색 
            while ll >=0 and rr < len(s) and s[ll] == s[rr]:
                if rr-ll+1 > max_len :
                    max_len = rr-ll+1
                    ans_ll = ll
                    ans_rr = rr
                ll-=1
                rr+=1

            ll = i
            rr = i+1

            # 짝수길이(center가 없는) 문자열 탐색
            while ll >=0 and rr <len(s) and s[ll] == s[rr]:
                if rr-ll+1 > max_len :
                    max_len = rr-ll+1
                    ans_ll = ll
                    ans_rr = rr
                ll-=1
                rr+=1
        return s[ans_ll:ans_rr+1]

