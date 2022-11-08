factorialOfNumberUsingFunction.py
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

n = input("Enter the Number for Factorial (Leass tan of equal t 100)   :  ")
n = int(n)
print(fac(n))
