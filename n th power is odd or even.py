def value(a,b):
    c=a**b
    if(c%2==0):
        print(c,"is even")
    else:
        print(c,"is odd")
        
a=int(input("enter the number:"))
b=int(input("enter the power:"))
value(a,b)
print(value)
        