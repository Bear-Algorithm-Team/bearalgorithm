class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0 
        max_frequency = 0
        longest_len = 0
        frequency_map = {}

        for end in range(len(s)):
            if s[end] in frequency_map:
                frequency_map[s[end]]+=1
            else:
                frequency_map[s[end]] = 1 
            
            max_frequency = max(max_frequency,frequency_map[s[end]])
            
            while end-start+1 - max_frequency > k and start<=end: # end-start+1 - max_frequency를 하면, 남은 수는 k를 이용하여 문자를 같도록 맞출 수 있다.
                frequency_map[s[start]] -= 1 # 남은 k 가 없기 때문에, start를 증가시켜 window의 크기를 줄인다.
                start +=1
                
            longest_len = max(longest_len, end-start + 1)
        return longest_len
