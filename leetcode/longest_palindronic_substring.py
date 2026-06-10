class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        length = 0
        for i in range(len(s)):
            odd_length = self.extractLengthPalindrome(i, i, s)
            even_length = self.extractLengthPalindrome(i, i+1, s)

            best = max(even_length, odd_length)
            if best > length:
                length = best
                start = i - (length - 1) // 2
        return s[start: start + length]

    def extractLengthPalindrome(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return (right - left) - 1
