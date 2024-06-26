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

# Generate public and private keys
def generate_keys(bits):                   
    p, q = large_prime(bits)                          # generate prime numbers for the bits required
    n = p * q 
    phi = (p - 1) * (q - 1)
    e = 65537                                         # common e
    while gcd(e, phi) != 1:                           # conditions of e
        break
    _, x, _ = extended_gcd(e, phi)
    d = x 
    if d<0:
        d+=phi
    return (e, n), (d, n)

# Encryption
def encrypt(message, public_key):  
    e, n = public_key
    encrypted_message = pow(message, e, n)             # eqaution for ciphertext
    return encrypted_message

# Decryption
def decrypt(encrypted_message, private_key):  
    d, n = private_key 
    decrypted_message = pow(encrypted_message, d, n)   # eqaution for decryption
    return decrypted_message

# Factorizing modulus
def factorize_modulus(n):
    for i in range(2, int(math.sqrt(n)) + 1):          # range of i 
        if n % i == 0:
            return i, n // i 

# check the brute force function
def check(d, public_key, encrypted_message):
    e, n = public_key
    decrypted_message = pow(encrypted_message, d, n)
    return decrypted_message

# brute force
def brute_force(public_key, encrypted_message):
    d = 2
    while True:
        decrypted_message = check(d, public_key, encrypted_message)
        if decrypted_message:                          # If decrypted message is not None
            return decrypted_message, d
        d += 1

        
def main():
    print("Welcome to RSA!\n")

    bits = int(input("Enter the Number of Bits for the Key: "))

    start_time = time.perf_counter()

    public_key, private_key = generate_keys(bits)
    print("\nPublic Key (e,n):", public_key)
    print("Private Key (d,n): ", private_key)

    plaintext = int(input("\nEnter the Message: "))

    encrypted_message = encrypt(plaintext, public_key)
    print("\nEncrypted Message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted Message: ", decrypted_message)

    p, q = factorize_modulus(public_key[1])

    end_time = time.perf_counter()
    
    print("Factorized Modulus (p, q):", (p, q))
    print("\nProgram Time: {:.6f} ms".format((end_time - start_time) * 1000))

    start_time = time.perf_counter()

    encrypted_message =  encrypt(plaintext, public_key)
    private_exponent = brute_force(public_key, encrypted_message)

    end_time = time.perf_counter()

    print("\nBrute Force Time: {:.6f} ms".format((end_time - start_time) * 1000))
    print("Private exponent d:", private_exponent)


if __name__ == "__main__":
    main()