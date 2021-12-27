a= [6, 8, 4, 3, 9, 56, 0, 34, 7, 15,12,23,45,34,67,89]
# a=[1,2,3,4,5,6,6]
b=[]
m=[]
i=1
count=0
while i<len(a):
    if count==4:
       m.append(b)
       b=[]
       count=1
    else:
        count+=1
        b.append(a[i])
    i=i+1
print(m)
