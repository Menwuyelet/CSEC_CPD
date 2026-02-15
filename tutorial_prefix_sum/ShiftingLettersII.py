class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        sum = [0]*(len(s)+1)
        for _ in shifts:
            if _[2] == 0:
                sum[_[0]] -= 1
                sum[_[1]+1] += 1
            elif _[2] == 1:
                sum[_[0]] += 1
                sum[_[1]+1] -= 1
        
        _sum = []
        _sum.append(sum[0])
        for i in range(1, len(sum)):
            _sum.append(_sum[i-1] + sum[i])
        ans = ""
        for i in range(len(_sum)-1):
            ans += chr((ord(s[i]) - ord('a') + _sum[i]) % 26 + ord('a'))
        return (ans)