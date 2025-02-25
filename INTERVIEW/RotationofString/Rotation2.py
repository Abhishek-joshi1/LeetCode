def rotation(s, d):
    n = len(s)
    d = d % n  # Ensure d is within [0, n-1]
    
    result = list(s)
    for i in range(n):
        result[i] = s[(i - d) % n]
    
    return ''.join(result)

print(rotation("abcde", 2))  # Output: "cdeab"
print(rotation("abcdefg", 7))  
print(rotation("abcdefghijklmnopqrstuvwxyz", 26)) 