# a=[1,2,[5,6],2,3,[8,9]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)





a=[1,2,[2,3],3,4,[4,[3,4,5],6],[2,[3,4,1],2]]
i=0
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    sum=sum+a[i][j][k]
                    k=k+1
            else:
                sum=sum+a[i][j]
            j=j+1
    else:
        sum=sum+a[i]
    i=i+1
print(sum)