#temperature converter
c='y'
while c=='y':
    a=int(input("Enter the temperature:"))
    temp=input("Enter the temperature you want to convert it to(fahrenheit/celsius):")
    if(temp=='celsius'):
        c=(a-32)*(5/9)
        print("The temperature in celsius is:",c)
    if(temp=='fahrenheit'):
        f=(a*(9/5))+32
        print("The temperature in celsius is:",f)
    c=input("Do you want to continue(y/n)?")    
    
