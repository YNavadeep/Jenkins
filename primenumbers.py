l=int(input("enter lower number"))
u=int(input("enter upper number"))
print("the prime numbers between ",l,"and",u,"are :")
for n in range(l,u+1):
    if n>1:
        for a in range(2,n):
            if (n%a==0):
                break
            else:
                print(n)
