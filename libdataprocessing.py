s1=[]
in1=[]
in2=[]
in3=[]
out=[]
mod=[]
s=input()
s=input()
while(s!="Borrowers"):    
    s1=s.split("~")
    in1.append(s1)
    s=input()
s=input()
while(s!="Checkouts"):
    s1=s.split("~")
    in2.append(s1)
    s=input()
s=input()
while(s!="EndOfInput"):
    s1=s.split("~")
    mod.append(s1[2])
    for k in in2:
        if(k[0]==s1[0]):
            mod.append(k[1])
    for k in in1:
        if(k[0]==s1[1]):
            a="~".join(k)
            mod.append(a)
    out.append(mod)
    mod=[]
    in3.append(s1)
    s=input()
out.sort()
for i in out:
    a="~".join(i)
    print(a)
    
