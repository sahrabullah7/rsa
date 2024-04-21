import random                                         # choosing random number
import math                                           # calculating eqautions
import time                                           # get time

# A prime function
def prime(n):  
    if n <= 1:                                        # no decimal / -ve no /1 in the range                                   
        return False
    elif n <= 3:                                      # 2,3 in the range                           
        return True
    elif n % 2 == 0 or n % 3 == 0:                    # factors of 2,3    
        return False 
    i = 5
    while i * i <= n:                                 # to get the rest of the prime numbers
        if n % i == 0 or n % (i + 2) == 0:          
            return False                            
        i += 6                                        # new i
    return True

# For generating large prime numbers
def large_prime(bits):                       
    while True:
        p = random.randint(2**(bits-1), 2**(bits))    # generate the 1st prime no
        q = random.randint(2**(bits-1), 2**(bits))    # generate the 2nd prime no
        if prime(p) and prime(q) and p != q:
            return p, q

# Greatest common divisor
def gcd(a, b):                                      
    while b != 0:
        a, b = b, a % b                               # replace a with the b, replace b with the remainder
    return a 

# Extended greatest common divisor
def extended_gcd(a, b):                             
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0   