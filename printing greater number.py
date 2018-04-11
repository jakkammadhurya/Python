a = int((input("enter the first number")))
b = int((input("enter the second number")))
c = int((input("enter the third number")))
if a>b and a>c:
    print ("Greater number is", a)
elif b>a and b>c:
    print("Greater number is", b)
elif c>a and c>b:
    print("Greater number is", c)
elif a==b and b==c:
    print ("all are equal")

