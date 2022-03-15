import csv
from list import *
from list2 import *
from m import *

#print("I am here at 1")

with open('emp.csv',mode='r') as file:
        c=csv.reader(file)
        l=[]
        for i in c:
            l.append(i)
            #print(l)
            print(i)
#print("I am here at 4")
for i in l:
    print(i)
Emp = {}
for i in range(len(l)):
    if i == 0:
        continue
    x =l[i][0]
    login = l[i][1]
    logout = l[i][4]
    brk = [l[i][2], l[i][3]]
    Emp[x] = [(login, brk[0]), (brk[1], logout)]
for i in Emp:
    print(i,Emp[i])
    
def arrangemeeting(a,b,s):
    #print(l[a])
    #print(l[b])
    x=convert24(l[a][1])
    y=convert24(l[b][1])
    temp=0;
    r=""
    e=min(s)
    li=[]
    li.append(a)
    li.append(b)
    isvalid=False
    dif=min(x)-min(y)
    if(dif>0):
        r=l[a][1]
        c=l[b][2]
        temp=min(r)
    else:
        r=l[b][1]
        c=l[a][2]
        temp=min(r)
    #print("starting time:",r)
    #print(temp)
    #print(e)
    end=e+temp
    z=mintoh(end)
    #print(z)
    #print("end time is",convert12(z))
    if(min(z)-min(convert24(c))>0):
        #print("meeting after lunch")
        x=l[a][3]
        y=l[b][3]
        c=l[a][4]
        d=l[b][4]
        #li=[a,b]
        dif=min(x)-min(y)
        if(dif>0):
            r=l[a][3]
            temp=min(x)
            #print(temp)
        else:
            r=l[b][3]
            temp=min(y)
        f=e+temp
        #print(e)
        #print(temp)
        #print(f)
        #print("starting time",r)
        z=mintoh(f)
        #print("ending time",z)
        #print(min(c),min(d),f)
        if(min(c)>=f and min(d)>=f):
            isvalid=True
        else:
            isvalid=False
        if(isvalid):
            print("meeting after lunch")
            print("starting time",r)
            print("ending time",z) 
            writer.writerow([li, r, z])
        else:
            print("cannot arrange")
        #print("end time is",convert12(z))
    else:
        print("meeting before lunch")
        print("starting time is:",r)
        #print(z)
        print("ending time is",z)
        writer.writerow([li, r, z])


#driver code  
print("see the emp details")
c=input("do you want to schedule a meeting y/n");
f = open('Meet.csv', 'w')
writer = csv.writer(f)
header = ["Employee Ids", "Meeting From", "Meeting To"]
writer.writerow(header)
while(c=='y'):
    x, y = input("select emp: ").split()
    t=input("enter meeting time in hh:mm ")
    arrangemeeting(int(x),int(y),t)
    c=input("do you want to schedule a meeting y/n");