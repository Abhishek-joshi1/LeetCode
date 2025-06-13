class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if word1 == "": return word2
        if word2 == "": return word1
        n, m = len(word1), len(word2)
        res = ''
        i = 0 
        while i < n or i < m:
            if i < n : res += word1[i]
            if i < m : res += word2[i]
            i += 1
        
        return res 

if __name__ == "__main__":
    mySol = Solution()
    print(mySol.mergeAlternately("abc", "pqr"))
    print(mySol.mergeAlternately("ab", "pqrs"))
    print(mySol.mergeAlternately("abcd", "pq"))