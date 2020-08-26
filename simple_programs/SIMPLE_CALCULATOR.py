ch=int(input('''ENTER ANY ONE OPTION OUT OF
                1)ADDITION
                2)SUBTRACTION
                3)MULTIPLICATION
                4)DIVISION'''))
print ("YOU HAVE SELECTED ",ch)
a=int(input("a="))
b=int(input("b="))
if(ch==1):
    res=a+b

elif(ch==2):
    res=a-b

elif(ch==3):
    res=a*b

elif(ch==4):
    if(b!=0):
        res=a/b
    else:
        print("TRY WITH VALID INPUTS")
        exit(0)
print(res)