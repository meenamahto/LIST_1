a=[[1,4,2],[4,6,5],[5,6,7],[6,8,9]]
i=0
while i<len(a):
    j=0
    max=0
    while j<len(a[i]):
        if a[i][j]>max:
            max=a[i][j]
        j=j+1
    print("first max=",max)
    j=0
    max1=0
    while j<len(a[i]):
        if a[i][j]>max1:
            if a[i][j]!=max:
                max1=a[i][j]
            j=j+1
    i=i+1
    print("second max=",max1)


