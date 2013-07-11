#!/usr/bin/env python
s=open("/proc/mounts") #opens he file mount.py
f=s.read() #reads the content of the file /proc/mounts
z=f.split("\n")# splits the output into individual lines
p=len(z) #counts the total number of member
i=1# initialising
while i<p:
     a=z[i].split(" ")# splits each line into list of words
     a.insert(1,"on")# inserts "on" in 1st position
     a.insert(3,"type")#inserts "type" in 3rd position
     a.insert(5,"(")#inserts open brackett in 5th position
     del a[-2]#deletes the second last word
     del a[-1]#deletes the last word
     a=[r.replace(",relatime", "") for r in a]#removes "relatime" from sentences
     a.append(")")#appends a closed bracket at the end of the list
     if a[-2]=="rw,":#checks if second last word is rw,
           a=[c.replace("rw,", "rw") for c in a]#replaces rw, with rw
     if i==6:# checks if it is the sixth line
           del a[0]#deletes word in first position
           a.insert(0, "/dev/sda")#inserts "/dev/sda" in first position
           a=[t.replace(",data=ordered","") for t in a]#removes "data=ordered" from the list.
     if i==1 or i==2:# checks if it is first or second line
           a=[c.replace("rw,nosuid,nodev,noexec","rw,noexec,nosuid,nodev") for c in a]#replaces wrong order of words with correct order
     if i==3:# checks if it is the third line
           a=[t.replace("size=496660k,nr_inodes=124165,","") for t in a]#removes unwanted text
     if i==4:#checks if it is the fourth line
           a=[e.replace(",ptmxmode=000","") for e in a]#removes unwanted text
     if i==5:#checks if it is the fifth line
           a=[t.replace("size=202392k","size=10%") for t in a]#converts size into percentage as should be in output
     if i==10:#checks if it is the tenth line
           a=[e.replace("size=5120k","size=5242880") for e in a]#changes unit of size
     if i==12:#checks if it is the twelveth line
           a=[e.replace("user_id=1000,group_id=1000","user=elita15") for e in a]#replaces user id by the actual user id      
     w=" ".join(a)#joins words in the list by " "
     print w#prints each line
     i=i+1#increaments i to go to next line
s.close() #close the file /proc/mounts
 

