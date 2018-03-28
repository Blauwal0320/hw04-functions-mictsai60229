# -*- coding: utf-8 -*-


def compute_gcd(a,b):

    while b!=0:
        a,b = b,a%b
        print(a,b)
    return a 


a = int(input("輸入第一個數字: "))
b = int(input("輸入第二個數字: "))
print(a, '和', b, '的最大公因數是', compute_gcd(a, b))
