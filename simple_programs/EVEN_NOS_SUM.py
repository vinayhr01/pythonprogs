num=int(input("ENTER LIMIT"))
sum=0
for num in range(0,num+1):
    if(num%2==0):
        sum=sum+num
        num=num+1
print(sum)