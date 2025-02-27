'''
Given a string s, the task is to reverse the string. Reversing a string means rearranging the characters such that the first character becomes the last, the second character becomes second last and so on.

Examples:

Input: s = “GeeksforGeeks”
Output: “skeeGrofskeeG”
Explanation : The first character G moves to last position, the second character e moves to second-last and so on.


Input: s = “abdcfe”
Output: “efcdba”
Explanation: The first character a moves to last position, the second character b moves to second-last and so on. 
'''

def reverse_String(st):
    res = []
    for i in range(len(st) - 1,-1,-1):
        res.append(st[i])
    return ''.join(res)

print(reverse_String("Abhishek"))
print(reverse_String("Karma"))