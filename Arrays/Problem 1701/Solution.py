class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str2 or not str1: return ""
        # res = ""
        # for i in range(min(len(str1),len(str2))):
        #     if str1[i] == str2[i]:
        #         res += str2[i]
        #     else:
        #         return res 
        # return res
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)
        
        if str1 + str2 != str2 + str1:
            return "" 
        
        res = gcd(len(str1), len(str2))
        return str1[:res]

if __name__ == "__main__":
    mySOl = Solution()
    print(mySOl.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
    print(mySOl.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))
    print(mySOl.gcdOfStrings(str1 = "LEET", str2 = "CODE"))