import importlib
import sys
import os
from io import StringIO
#basic fibo test
def test_fibo(fibo): #module
    answer = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,832040]
    try:
        for i in range(31):
            if fibo.compute_fibonacci(i) != answer[i]:
                return 0
        return 30
    except:
        return 0
    
def test_prime(prime):
    score = 20
    prime_number = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    not_prime_number = [1,4,6,8,9,10,12,14,15,16,18,20,21,22,24,25,26,27,28,30,32,33,34,35,36,38,39,40,42,44,45,46,48,49,50,51,52,54,55,56,57,58,60,62,63,64,65,66,68,69,70,72,74,75,76,77,78,80,81,82,84,85,86,87,88,90,91,92,93,94,95,96,98,99,100]
    try:
        for num in prime_number:
            if not prime.is_prime(num):
                score-=10
                break
        for num in not_prime_number:
            if prime.is_prime(num):
                score-=10
                break
    except:
        return 0
    
    return score

def test_GCD(gcd):
    test_data = [(0,3),(3,0),(48,49),(383,541),(1001,133)]
    answer = [3,3,1,1,7]
    
    try:
        for (a,b),s  in zip(test_data,answer):
            if gcd.compute_gcd(a,b) != s:
                return 0
        return 20
    except:
        return 0

def test_all(fibo,gcd,prime):
    
    ans_prime = [2,3,5,13,89,233,1597]
    ans_not_prime = [1,8,21,34,55,144,377,610,987,2584,4181,6765]
    ans_gcd = [1,2,3,5,2,13,21,34,55,1,6,1,377,10,21,1,646,37,6765]
    test_number = 304250263527210
    
    try:
        student_prime = []
        student_not_prime = []
        student_gcd = []
        for n in range(2,21):
            num = fibo.compute_fibonacci(n)
            if prime.is_prime(num):
                student_prime.append(num)
            else:
                student_not_prime.append(num)
            student_gcd.append(gcd.compute_gcd(test_number,num))
            
        if student_prime == ans_prime and student_not_prime == ans_not_prime and student_gcd ==ans_gcd:
            return 10
    except:
        pass
    
    return 0


if __name__=="__main__":
    directory = "hw4_" + sys.argv[1] + ".build."
    scores = []
    oldstdin = sys.stdin
    sys.stdin = StringIO('1\n1\n1\n1\n2\n3\n4\n5\n6\n')
    with open("hw4_"+sys.argv[1]+"/score","w") as f:
        fibo,prime,gcd = None,None,None
        try:
            fibo = importlib.import_module(directory+"hw4_fibo")
            scores.append(test_fibo(fibo))
        except:
            scores.append(0)
        try:
            prime = importlib.import_module(directory+"hw4_prime")
            scores.append(test_prime(prime))
        except:
            scores.append(0)
            
        try:
            gcd = importlib.import_module(directory+"hw4_gcd")
            scores.append(test_GCD(gcd))
        except:
            scores.append(0)
            
        if fibo!=None and prime!=None and gcd!=None:
            try:
                scores.append(test_all(fibo,gcd,prime))
            except:
                scores.append(0)
        else:
            scores.append(0)
        sum = 0
        testcase = ["fibo","prime","gcd","all"]
        for score,case in zip(scores,testcase):
            f.write(str(score)+",")
            print("%s : %d" %(case,score))
            sum+=score
        print("sum : %d" %(sum))
        f.write(str(sum))
        
