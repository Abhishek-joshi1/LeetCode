class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        l = 0
        max_length = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            max_length = max(max_length, r - l + 1)
        return max_length

if __name__ == "__main__":
    mySol = Solution()
    print(mySol.lengthOfLongestSubstring("abcabcbb"))
    print(mySol.lengthOfLongestSubstring("bbbbb"))
    print(mySol.lengthOfLongestSubstring("pwwkew"))
                
                