# -*- coding: utf-8 -*-

fibo = [0,1]
counter = 1

def compute_fibonacci(num):
    if num <= compute_fibonacci.counter:
        return compute_fibonacci.fibo[num]
    else:
        for i in range(counter+1,num+1):
            result = compute_fibonacci.fibo[i-1] + compute_fibonacci.fibo[i-2]
            compute_fibonacci.fibo.append(result)
        return result
compute_fibonacci.counter = 1
compute_fibonacci.fibo = [0,1]
num = int(input("你想看費氏數列第幾個數字？ "))
print('費氏數列第', num, '個數字是', compute_fibonacci(num))
