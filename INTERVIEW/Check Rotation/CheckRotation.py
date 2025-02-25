'''
Check if Strings Are Rotations of Each Other
Given two string s1 and s2 of same length, the task is to check whether s2 is a rotation of s1.

Examples: 

Input: s1 = “abcd”, s2 = “cdab”
Output: true
Explanation: After 2 right rotations, s1 will become equal to s2.


Input: s1 = “aab”, s2 = “aba”
Output: true
Explanation: After 1 left rotation, s1 will become equal to s2.


Input: s1 = “abcd”, s2 = “acbd”
Output: false
Explanation: Strings are not rotations of each other.
'''

def is_Rotated(s1, s2):
    n = len(s1)
    m = len(s2)
    if n != m:
        return False
    for _ in range(n):
        s1 = s1[-1] + s1[0:n-1]
        if s1 == s2:
            return True 
    return False

print(is_Rotated("aba","aab"))
print(is_Rotated("abcd","acdb"))