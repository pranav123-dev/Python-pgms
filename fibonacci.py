n=int(input("Enter the number of the terms:"))
a,b=0,1
print("Fibonacci series:")
for i in range(n):
    print(a)
    a,b=b,a+b