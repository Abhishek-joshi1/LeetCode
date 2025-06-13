from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:return True
        for i in range(len(flowerbed)):
            if (flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == (len(flowerbed) - 1) or flowerbed[i + 1] == 0)):
                n -= 1
                flowerbed[i] = 1
        return n == 0

if __name__ == "__main__":
    mySOl = Solution()
    print(mySOl.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
    print(mySOl.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2)) 