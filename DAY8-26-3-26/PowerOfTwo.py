# Power of two (any number that can be represented by 2 powers ex:2,4=2^2,8=2^3.....)

def powOfTwo(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:     # checks divisibility
        return False
    return powOfTwo(n//2)    

print(powOfTwo(16))
print(powOfTwo(35))
print(powOfTwo(3))
print(powOfTwo(64))

