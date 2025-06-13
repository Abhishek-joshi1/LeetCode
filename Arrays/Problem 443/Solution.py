from typing import List 
class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        
        write = 0
        i = 0
        while i < len(chars):
            char = chars[i]
            cnt = 1
            
            while i + 1 < len(chars) and char == chars[i + 1]:
                cnt += 1
                i += 1
            
            chars[write] = char
            write += 1
            
            if cnt > 1:
                for c in str(cnt):
                    chars[write] = c
                    write += 1
            
            i += 1
        
        return write 

if __name__ == "__main__":
    mySol = Solution()
    result = mySol.compress(["a","a","b","b","c","c","c"])
    print(result)
