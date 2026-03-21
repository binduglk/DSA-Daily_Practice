'''Given a string, find the first character that appears only once. Return its index. 
If no unique character exists, return -1.
s = "leetcode" → Output: 0 (l appears only once, at index 0) s = "loveleet" → Output: 2 (v appears only once, at index 2) 
s = "aabb" → Output: -1 (no unique character)'''

def firstuniquechar(s):
    count = {}

    for char in s:                  # count every character
        count[char] = count.get(char, 0) + 1

    for i,char in enumerate(s):           # find first with count 1
        if count[char] == 1:                # return index of once letter
            return i
    return -1              # if no one number appeared once 

print(firstuniquechar('leetcode'))
print(firstuniquechar('nandini'))