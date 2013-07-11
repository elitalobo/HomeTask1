:#!/usr/bin/env python
s=open("/proc/mounts") #opens he file mount.py
f=s.read() #reads the content of the file /proc/mounts
z=f.split("\n")
p=len(z) #counts the total number of member
i=1
while i<p:
     a=z[i].split(" ")
     a.insert(1,"on")
     a.insert(3,"type")
     a.insert(5,"(")
     del a[-2]
     del a[-1]
     a=[r.replace(",relatime", "") for r in a]
     a.append(")")
     if a[-2]=="rw,":
           a=[c.replace("rw,", "rw") for c in a]
     if i==6:
           del a[0]
           a.insert(0, "/dev/sda")
           a=[t.replace(",data=ordered","") for t in a]
     if i==1 or i==2:
           a=[c.replace("rw,nosuid,nodev,noexec","rw,noexec,nosuid,nodev") for c in a]
     if i==3:
           a=[t.replace("size=496660k,nr_inodes=124165,","") for t in a]
     if i==4:
           a=[e.replace(",ptmxmode=000","") for e in a]
     if i==5:
           a=[t.replace("size=202392k","size=10%") for t in a]
     if i==10:
           a=[e.replace("size=5120k","size=5242880") for e in a]
     if i==12:
           a=[e.replace("user_id=1000,group_id=1000","user=elita15") for e in a]       
     w=" ".join(a)
     print w
     i=i+1
s.close() #close the file /proc/mounts
 

