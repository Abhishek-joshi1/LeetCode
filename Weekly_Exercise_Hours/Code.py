class Solution:
    def Exercise_Tracker():
        n = 7
        arr = []
        for i in range(n):
            print("Day " + str(i + 1) + " Exercise Duration (minutes): ")
            curr = int(input())
            arr.append(curr)
        
        Total_Exercise_Hours = float(sum(arr))
        Avg_Ex_hrs = Total_Exercise_Hours / 7.0
        print(f"Total Exercise Hours : {Total_Exercise_Hours} minutes")
        print(f"Average Exercise Hours : {Avg_Ex_hrs} minutes")

if __name__ == "__main__":
    s = Solution()
    s.Exercise_Tracker()