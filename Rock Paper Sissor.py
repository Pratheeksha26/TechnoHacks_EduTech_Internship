import numpy as np
while True:
    a=np.random.choice(['rock','paper','sissor'])
    c=input("Enter your choice(rock/paper/sissor):")
    print("The Computers choice:",a)
    if (((a=='rock')and(c=='paper'))or((a=='paper')and(c=='sissor'))or((a=='sissor')and(c=='rock'))):
        print("You win")
    elif(((a=='rock')and(c=='rock'))or((a=='paper')and(c=='paper'))or((a=='sissor')and(c=='sissor'))):
        print("Its a tie")
    else:
        print("I win")
    d=input("Do you want to continue(y/n)?")
    if (d!='y'):
        break

