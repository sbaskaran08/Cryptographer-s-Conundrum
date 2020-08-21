a=input()
length=len(a)//3
name0='PER'
name=name0*int(length)
count=0
j=0
for i in a:
    if(i!=name[j]):
        count=count+1
    j=j+1
print(count)
        
    
