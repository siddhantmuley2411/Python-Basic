#Q.1

list=[]

for i in range(1,51):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            list.append(i)
            

print(list)
