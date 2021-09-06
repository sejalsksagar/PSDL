#3372 06/09/21
#Ass0: 1. Write a program to generate SI

p = float(input("Principal amount: "))
n = float(input("No. of years: "))
r = float(input("Rate of interest: "))

si = p * n * r / 100

print("Simple interest = ", si)
