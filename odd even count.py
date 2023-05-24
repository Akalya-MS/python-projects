even_count=0
odd_count=0

n=int(input("enter n:"))
m=int(input("enter m:"))

for i in range(n,m+1):
    if(i%2==0):
        even_count=even_count+1
        
    else:
        odd_count=odd_count+1
        
print("even count is",even_count)
print("odd count is",odd_count)