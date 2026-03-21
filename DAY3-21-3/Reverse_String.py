'''Given a list of characters, reverse it in-place. You must do it with O(1) extra space — no creating a new list.
Input : ['h','e','l','l','o'] → Output: ['o','l','l','e','h'] 
Input : ['A','n','n','a'] → Output: ['a','n','n','A']'''

def reversestring(s):
    left = 0
    right = len(s) - 1        # len = 5 , then right = 4

    while left < right: 
        s[left], s[right] = s[right], s[left]     # swap
        left += 1
        right -= 1
         
    return s                    # WHEN THE POINTERS COME TO MIDDLE IT STOPS 

print(reversestring(['h','e','l','l','o']))
print(reversestring(['a','n','n','a']))
print(reversestring(['r','o','s','e']))