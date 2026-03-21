'''Two strings are anagrams if they have the exact same letters in the same quantity — 
just in a different order. Return True if they are anagrams, False if not.
s = "anagram", t = "nagaram" → True s = "rat", t = "car" → True 
s = "hello", t = "world" → False s = "listen", t = "silent" → True'''

def anagram(s, t):
    if len(s) != len(t):
        return False
    count = {}

    for char in s:
        count[char] = count.get(char,0)+1
    
    for char in t:
        count[char] = count.get(char,0)-1

    for val in count.values():
        if val != 0:
            return False
    
    return True
print(anagram("car","rat"))
print(anagram("listen","silent"))

