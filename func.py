
'''
def add (a,b):
    print(a+b)
    add(5,6)

print("yuvraj chavan")
a=5
b=6
sum=a+b 
print("sum",sum)

a=int(input("Enter number"))
if(a%2==0):
    print("even")
else:
    print("odd")

#even odd number---
def check(n):
    if n % 2 == 0:
        print("even")
    else: 
        print("odd")
     
        check(2) 
'''

#factorial n number
def fact (n):
 return 1 if (1==0 or n==0 ) else n*fact(n-1)


print(fact(5))
#fact 4!=1*2*3*4