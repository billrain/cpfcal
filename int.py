import math
#Python program to compute compound interest using function

def compoundInterest(p, r, t):
    ci = p * (pow((1 + r / 100), t))
    return ci


p = float(input("Enter the principal amount : "))

t = float(input("Enter the number of years : "))

r = float(input("Enter the rate of interest : "))

#call compound interest
ci =  compoundInterest(p, r, t)

i = 1
while i < t: 

#print
print("Compound interest : {}".format(ci))
