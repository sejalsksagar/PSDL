#3372 16/09/21
#Ass1 A: Write a program to find Factorial of a Number in Python

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
    
num = int(input("Enter a number: "))
print("Factorial of "+str(num)+" is "+str(factorial(num)))

#Ass1 B: Write a Python Program to Accept n numbers from users and display average, sum of these numbers 

def accept():
    print("Enter numbers:")
    num_list = list(map(int, input().split()))
    return num_list
    
def result(L):
    print("Average = "+str(sum(L)/len(L)))
    print("Sum = "+str(sum(L)))

    
L = accept()
result(L)
