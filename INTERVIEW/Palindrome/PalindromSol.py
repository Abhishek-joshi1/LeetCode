'''
Given a string s, the task is to check if it is palindrome or not.

Example:

Input: s = “abba”
Output: 1
Explanation: s is a palindrome


Input: s = “abc” 
Output: 0
Explanation: s is not a palindrome
'''

def is_palindrome(s):
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    
    left = 0
    right = len(cleaned_s) - 1
    
    while left < right:
        if cleaned_s[left] != cleaned_s[right]:
            return False
        left += 1
        right -= 1
    
    return True

print(is_palindrome("abba"))  
print(is_palindrome("abc"))   