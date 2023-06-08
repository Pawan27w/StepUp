import sys

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for f in fib():
    if f>100:
        break
    print(f)



sys.exit(0)
#generate first n number

def number(num):
    print("numbering started")
    n=1
    while n<=num:
        yield n
        n=n+1
values=number(5)
for i in values:
    print(i)



sys.exit(0)

def countdown(num):
    print("countdown started")
    while(num>0):
        yield num
        num=num-1

values=countdown(5)
for i in values:
    print(i)


sys.exit(0)

def my_gen():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'

g=my_gen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))



sys.exit(0)
def decor(func):
    def inner(name):
        if name=="Sunny":
            print("Hello Sunny Bad Morning")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("Hello",name,"Good Morning")

wish("Durga")
wish("Ravi")
wish("Sunny")


sys.exit(0)

def decor(func):
    def inner(name):
        if name=="sunny":
            print("hello sunny bad morning")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("hello",name,"good morning")

wish("durga")
wish("pawan")
wish("sunny")

sys.exit(0)

def outer():
    print("outer start")

    def inner():
        print("inner")
    print("outer call")
    inner()
outer()




sys.exit(0)
from functools import *

I=[10,20,30,40]
result=reduce(lambda x,y:x+y,I)
print(result)

sys.exit(0)
I=[10,40,12,42,32,55]
l1=list(filter(lambda x:x%2==0,I))
print(l1)


sys.exit(0)

def is_even(x):
    if x%2==0:
        return True
    else:
        return False
I=[10,40,12,42,32,55]
l1=list(filter(is_even,I))
print(l1)


sys.exit(0)
# to find max value

s=lambda a,b:a if a>b else b
print(s(10,20))



sys.exit(0)
s=lambda n:n*n
print(s(4))
b=lambda a,b:a+b
print(b(20,30))


sys.exit(0)

# recursive function
def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result
print(fact(4))


sys.exit(0)
def display(**kwargs):
    for k,v in kwargs.items():
        print(k,"=",v)
display(a=10,b=20,c=30)
display(rno=1,name="gogi",add="pune",sub="python")

sys.exit(0)

def sum(*n):
    total=0
    for n1 in n:
        total=total+n1
    print("the sum=",total)
sum(10,20,3,40,50)


sys.exit(0)

def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=calc(50,12)
print("the result")
for i in t:
    print(i)



sys.exit(0)

def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
x,y=sum_sub(100,50)
print("sum",x)
print("sub",y)



sys.exit(0)

def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
for i in range(1,5):
    print("factorial of",i,"is",fact(i))


sys.exit(0)

def even_odd(num):
    if num%2==0:
        print(num,"even number")
    else:
        print(num,"odd number")

even_odd(65)
even_odd(66)

sys.exit(0)

def add(x,y):
    return x+y
result=add(10,20)
print(result)
print(add(20,30))
# print("sum is")

sys.exit(0)

def sqr(a,b):
    print("the suare of",a,b,"is",a*b)

sqr(10,20)
sqr(20,30)



sys.exit(0)
def wish(name):
    print("hello",name,"good morning")
wish("pawan")

sys.exit(0)

l=[100,200,300,250,500,516,101]
for i in l:
    if i>=500:
        print("this order must required insurance")
        continue
    print(i)

sys.exit(0)

for i in range(10):
    if i==7:
        print("processing is enough")
        break
    print(i)

sys.exit(0)


d={}
d[101]="shyam"
d[102]="ram"
d[103]="ganesh"
print(d)
