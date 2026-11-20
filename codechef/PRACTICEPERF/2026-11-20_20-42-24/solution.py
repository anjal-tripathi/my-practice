# cook your dish here
p1,p2,p3,p4=map(int,input().split())
ls=[]
ls.extend([p1,p2,p3,p4])
count=0
for i in ls:
    if i>=10:
        count=count+1
print(count)        