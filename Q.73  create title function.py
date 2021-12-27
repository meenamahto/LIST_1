a=["meena", "is", "here"]
    
# m=a[0].split()
# print(m)
d=[]
for i in range(len(a)):
    s=''
    for j in range(len(a[i])):
        if j==0:
            s=s+a[i][0].upper()
        else:
            s=s+a[i][j]
    d.append(s)
print(d)

