#!/usr/bin/env python
import sys 
def readfile():#defining readfile function
   s=open("/proc/mounts") #opens the file mount.py
   f=s.read() #reads the content of the file /proc/mounts
   z=f.split("\n")# splits the output into individual lines
   changefile(z)# calling changefile function
   s.close()
def changefile(z):#defining changefile function
   p=len(z)#counts no of lines
   i=1#initiation
   while i<p:
       a=z[i].split(" ")# splits each line into list of words
       a.insert(1,"on")# inserts "on" in 1st position
       a.insert(3,"type")#inserts "type" in 3rd position
       a.insert(5,"(")#inserts open brackett in 5th position
       del a[-2]#deletes the second last word
       del a[-1]#deletes the last word
       a.append(")")#appends a closed bracket at the end of the list 
       w=" ".join(a)#joins words in the list by " "
       print w#prints each line
       i=i+1#increaments i to go to next line

if __name__ == '__main__':#to open readfile
   readfile()
   sys.exit(0)
  

