import os
f=open('compiler_design.py','r')
data=f.read()
s=""
for i in data:
    if i=='=' or i=="[" or i=="]" or i==")" or i=="(" or i=="." or i=="{" or i=="}" or i==":" or i==";":
        s=s+" "
    else:
        s=s+i
l=s.split(" ")
ans=[]
count=0
for i in l:
    if i=='\nl' or i=='':
        continue
    elif i=='\nprint':
        if count==0:
            ans.append("print")
            count+=1
    else:
        if i not in ans:
            ans.append(i)
print(ans)
