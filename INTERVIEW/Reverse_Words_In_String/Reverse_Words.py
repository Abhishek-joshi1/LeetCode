'''
Reverse Words in a String 
Given a string str, the task is to reverse the order of the words in the given string. Note that str may contain leading or trailing dots(.) or multiple trailing dots(.) between two words. The returned string should only have a single dot(.) separating the words.

Examples:

Input: str = “i.like.this.program.very.much” 
Output: str = “much.very.program.this.like.i” 


Input: str = ”..geeks..for.geeks.” 
Output: str = “geeks.for.geeks”
'''

def reverse_words(st): 
    words = [word for word in st.split('.')]
    words.reverse()
    return '.'.join(words)

print(reverse_words("i.like.this.program.very.much"))
print(reverse_words("..geeks..for.geeks."))