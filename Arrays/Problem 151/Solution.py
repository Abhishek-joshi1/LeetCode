class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        s = s.strip().split()
        return " ".join(s[::-1])
    
if __name__ == "__main__":
    mySOl = Solution()
    print(mySOl.reverseWords(s = "the sky is blue")) 
    print(mySOl.reverseWords(s = "  hello world  "))
    print(mySOl.reverseWords(s = "a good   example"))