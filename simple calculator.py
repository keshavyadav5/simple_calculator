
print('\t\t\tSIMPLE CALCULATOR')
print('\tHere you can perform[+,-,*,/,%,pow,sin,cos,tan]')
print("\t\t 'exit' to break the loop")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
import math
def sum(a,b):
    a+=b
    return a
def sub(a,b):
    a-=b
    return a
def mult(a,b):
    a*=b
    return a
def div(a,b):
    a/=b
    return a
def mod(a,b):
    a%=b
    return a
def pow(a,b):
    a=math.pow(a,b)
    return a
def sin(a):
    a=math.radians(a)
    a=math.sin(a)
    return a
def cos(a):
    a=math.radians(a)
    a=math.cos(a)
    return a
def tan(a):
    a=math.radians(a)
    a=math.tan(a)
    return a
try:
    while(1):
        a=input("Enter 1st value: ",)
        if a=='exit':
            break
        a=int(a)
        o=input("enter operator for calculation: ")
        if o=='exit':
            break
        else:
            if o=='+':
                b=int(input('Enter 2nd number: '))
                s=sum(a,b)
                print('Sum =',s)
            elif o=='-':
                b=int(input('Enter end number: '))
                s=sub(a,b)
                print('Subtraction:',s)
            elif o=='*':
                b=int(input('Enter end number: '))
                s=mult(a,b)
                print('Multiplication:',s)
            elif o=='/':
                b=int(input('Enter end number: '))
                s=div(a,b)
                print('Division:',s)
            elif o=='%':
                b=int(input('Enter end number: '))
                s=mod(a,b)
                print('Modulus:',s)
            elif o=='^':
                b=int(input('Enter 2nd number: '))
                s=pow(a,b)
                print(f'{a} power {b} :',s)
            elif o=='sin':
                s=sin(a)
                print(f'sin({a}):',s)
            elif o=='cos':
                s=cos(a)
                print(f'cos({a}):',s)
            elif o=='tan':
                s=tan(a)
                print(f'tan({a}):',s)
except:
    print("something went wrong")

