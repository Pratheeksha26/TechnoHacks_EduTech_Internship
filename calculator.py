def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

c='y'
while c=='y':
    print("1. ADD \n2. SUBTRACT \n3. MULTIPLY \n4. DIVIDE")
    choice=int(input("Enter the choice:"))
    a=int(input("Enter the value:"))
    b=int(input("Enter the value:"))
    if choice==1:
        print("The sum is: ",add(a,b))
    elif choice==2:
        print("The remainder is: ",sub(a,b))
    elif choice==3:
        print("The product is: ",mul(a,b))
    elif choice==4:
        print("The quotient is: ",div(a,b))
    else:
        print("INVALID CHOICE!!")
    c=input("Do you want to continue?(y/n): ")
