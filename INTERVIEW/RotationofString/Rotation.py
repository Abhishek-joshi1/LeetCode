'''

LEFT ROTATION OF A STRING 
Given a string s and an integer d, the task is to left rotate the string by d positions.

Examples:

Input: s = “GeeksforGeeks”, d = 2
Output: “eksforGeeksGe”  
Explanation: After the first rotation, string s becomes “eeksforGeeksG” and after the second rotation, it becomes “eksforGeeksGe”.


Input: s = “qwertyu”, d = 2 
Output: “ertyuqw” 
Explanation: After the first rotation, string s becomes “wertyuq” and after the second rotation, it becomes “ertyuqw”.
'''

def rotation(s, d):
    s = list(s)
    for i in range(d):
        first = s[0]
        for i in range(len(s) - 1):
            s[i] = s[i + 1]
        s[-1] = first
    
    return ''.join(s)

print(rotation("qwertyu",2))
print(rotation("GeeksforGeeks",4))