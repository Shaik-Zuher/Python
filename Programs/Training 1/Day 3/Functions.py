'''
Syntax:
def funname():
    //block
funname()----calling
'''

#write a function which takes 2 arguments a and b typecast the value of 2nd argument into integer then multiply both the arguments and print the last digit of the result
'''
def typer(a,b):
    b=int(b)
    mul=a*b
    last=mul%10
    print(last)

typer(1,2)
'''
#Write programs for different types of arguments
'''
"""positional"""
def position(num):
    print("This is called:",num)
position(6)
"""key argumnets"""
def key(name,clas):
    print("This is",name,"from",clas,"class")
key(clas="8th",name="chakri")
"""default arguments"""
def default(a=5,b=10):
    print(a+b)
default()
default(4,10)
"""unknown args in js ...args"""
"""unknown arguments arguments stored in dictionary format"""
def unknown(**train):
    print("Train Number",train["traino"],train["trainname"])
unknown(trainname="sarkar",traino=1890)
'''
#Write function to calculate sum of first and last digit of  a number number must be taken as argumnet input 785 output 12
'''
def add(a):
    last=a%10
    num=a
    result=0
    while(num>0):
        rem=num%10
        result=result*10
        result=result+rem
        num=num//10
    first=result%10
    print(first+last)
add(785)
'''
def add(a):
    last=a%10
    while a>10:
        a=a//10
    print(last+a)
add(785)
    
