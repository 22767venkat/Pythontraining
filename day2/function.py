
#rock
def rps(p1,p2):
    if(p1=='r' and p2=='s') or (p1=='s' and p2=='p') or (p1=='p' and p2=='r'):
        print('player1 won')
    elif(p2=='r' and p1=='s') or (p2=='s' and p1=='p') or (p2=='p' and p1=='r'):
        print('player2 won')
    elif(p1==p2):
        print("it's a tie break")
    else:
        print('given a unsuthorised sign')
result=rps("r","r")







#largest
def lar(n1,n2,n3):
    if(n1>n2>n3):
        print('n1 largest no')
    elif(n1<n2>n3):
         print('n2 largest no')
    else:
        print('n3 largest no')
result=lar(1100,2000,0)



#count
def count(input):
    l1 = input.split()
    print(len(l1))
print("Word count for Sonata Software Ltd Hyderabad is")
result=count("Sonata Software Ltd hyderabad")



#palindrom
def palindrom(n):
    temp=n
    rev=0
    while(n>0):
        a=n%10
        rev=rev*10+a
        n=n//10
    if(temp==rev):
        print('the number is palindrom!')
    else:
        print('not a palindrom!')
result=palindrom(999)




#birth
def century(by):
    py=2022
    cen=100-(py-by)
    print(cen)
print("years to complete to reach 100 for a person born in 1999 are")
result=century(1999)



