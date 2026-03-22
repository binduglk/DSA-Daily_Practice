'''You are climbing a staircase with n steps. Each time you can climb either 1 step or 2 steps. 
How many distinct ways can you reach the top?
n = 2 → Output: 2 Ways: [1+1] or [2] 
n = 3 → Output: 3 Ways: [1+1+1] or [1+2] or [2+1] n = 5 → Output: 8'''

def climbstaris(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    prev2 = 1    # ways to reach step 1
    prev1 = 2    # ways to reach step 2

    for i in range(3,n+1): # range stops before the end number so it is n+1
        current = prev2 + prev1 
        prev2 = prev1 
        prev1 = current
    
    return prev1

print(climbstaris(5))
print(climbstaris(8))
