a=[1,"5","python",45,45.3]
i=0
b=[]
while i<len(a):
    if type(a[i])==float:
        b.append(a[i])
    i=i+1
print(b)
