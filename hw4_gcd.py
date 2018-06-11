# -*- coding: utf-8 -*-


def compute_gcd(a,b):
    gcd = 1
    for i in range( gcd+1, min(num_a, num_b)+1 ):
        if num_a % i == 0 and num_b % i == 0:
            gcd = i

a = int(input("輸入第一個數字: "))
b = int(input("輸入第二個數字: "))
print(a, '和', b, '的最大公因數是', compute_gcd(a, b))
