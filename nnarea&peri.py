num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if num1>=num2 and num1>=num3:
    n=num1
elif num2>=num1 and num2>=num3:
    n=num2
else:
    n=num3
print(f"The biggest number is:{n}")
nn=n**2
nnn=n**3
result=n+nn+nnn
print(f"n+nn+nnn={n}+{nn}+{nnn}={result}")
radius=n
area=3.14*radius*2
perimeter=2*3.14*radius
print(f"For circle with radius{radius}:")
print(f"Area={area:02f}")
print(f"Perimeter={perimeter:02f}")