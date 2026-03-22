'''You are given a number represented as an array of digits. 
Add 1 to the number and return the result as an array.
Input : [1, 2, 3] → Output: [1, 2, 4] (123 + 1 = 124) 
Input : [1, 2, 9] → Output: [1, 3, 0] (129 + 1 = 130) 
Input : [9, 9, 9] → Output: [1, 0, 0, 0] (999 + 1 = 1000) Input : [9] → Output: [1, 0] (9 + 1 = 10)'''

def plusone(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i] < 9:
            digits[i] += 1   # just add one carry
        return digits

        digits[i] = 0       # digit was 9 → becomes 0, carry to next
    
    return [1] + digits     # all digits were 9 eg: 999 → 1000

print(plusone([1,2,3,4]))