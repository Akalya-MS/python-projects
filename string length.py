a=input("enter the string:")
b=len(a)
if b%5==0:
    c=a.upper()
    print(c)
    d=a[::-1]
    print(d)
else:
    print("length is not a multiple of five")