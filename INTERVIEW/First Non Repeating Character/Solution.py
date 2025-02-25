'''
First Non Repeating Character in a String 
Given a string s of lowercase English letters, the task is to find the first non-repeating character. If there is no such character, return ‘$’.

Examples: 

Input: s = “geeksforgeeks”
Output: ‘f’
Explanation: ‘f’ is the first character in the string which does not repeat.


Input: s = “racecar”
Output: ‘e’
Explanation: ‘e’ is the only character in the string which does not repeat.


Input: “aabbccc”
Output: ‘$’
Explanation: All the characters in the given string are repeating.
'''
from collections import Counter
def first_non_Repeating(s1):
    count = Counter(s1) 
    for c in s1:
        if count[c] == 1:
            return c
    return '$'

print(first_non_Repeating("aaabbbbcddd"))
print(first_non_Repeating("abbbbcdeeffgh"))
print(first_non_Repeating(""))