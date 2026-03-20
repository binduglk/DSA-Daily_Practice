# A palindrome reads the same forwards and backwards. Given a sentence, check if it's a palindrome —
# but ignore spaces, punctuation, and treat uppercase/lowercase as same.
# Input : "racecar" → True (racecar = racecar backwards) Input : "hello" → False (olleh ≠ hello)
# Input : "A man a plan Panama" → True (amanaplanacanalpanama) Input : "Deepika" → False (try it yourself!)


def palindrome(s):

    cleaned = [] # empty list to store char
    for char in s:
        if char.isalnum(): # keeps only alphabets n numbers
            cleaned.append(char.lower()) # converts to lower

    cleaned_str = "".join(cleaned) # combines all char into one string
    return cleaned_str == cleaned_str[::-1] # reverse the string

print(palindrome("racecar"))
print(palindrome("man"))


