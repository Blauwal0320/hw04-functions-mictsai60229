# -*- coding: utf-8 -*-

import math
def is_prime(num):
    if num <=is_prime.largest:
        if num in is_prime.prime_number:
            return True
        else:
            return False
    sqrt_num = int(math.floor(math.sqrt(num)))
    #checking prime
    for n in is_prime.prime_number:
        if num%n == 0:
            return False
    for n in range(is_prime.largest+1 ,sqrt_num+1):
        check_n = True
        sqrt_n = math.floor(math.sqrt(n))
        for p in is_prime.prime_number:
            if sqrt_n < p:
                break
            if n % p == 0:
                check_n = False
                break
        if check_n:
            is_prime.prime_number.append(n)
        is_prime.largest += 1

        if num%n == 0:
            return False
    return True
is_prime.prime_number = [2]
is_prime.largest = 2

num = int(input("Enter a number: "))

if is_prime(num):
    print(num, 'is a prime number.')
else:
    print(num, 'is not a prime number.')
