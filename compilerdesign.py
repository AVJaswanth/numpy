suffix=[]
proper_suffix=[]
prefix=[]
ans=input("Enter the string: ")
suffix.append("epsilon")
for i in range(1,len(ans)+1,1):
    if(i!=len(ans)):
        proper_suffix.append(ans[:i])
    suffix.append(ans[:i])
for i in range(1,len(ans)+1):
    prefix.append(ans[len(ans)-i:])
print(f"Suffix: {suffix}")
print(f"Proper Suffix: {proper_suffix}")
print(f"Prefix: {prefix}")
