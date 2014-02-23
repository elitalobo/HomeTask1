Mount v2
----------

**Task**
Write a file mount.py which when executed as ./mount.py gives the same output as mount command. For this we require to read /proc/mounts.

Code Description
--------------------

**readfile Function**

#. s=open("/proc/mounts")     opens  the file mount.py
#. f=s.read()                 reads the content of the file /proc/mounts
#. z=f.split("\n")            splits  the output into individual lines
#. changefile(z)              calls the  changefile function
#. s.close()                  close /proc/mount file

**changefile Function**

#.  p=len(z)                 counts no of lines
#.  a=z[i].split(" ")        splits each line into list of words
#.  a.insert(1,"on")         inserts "on" in 1st position 
#.  a.insert(3,"type")       inserts "type" in 3rd position
#.  a.insert(5,"(")          inserts open brackett in 5th position
#.  del a[-2]                deletes the second last word
#.  del a[-1]                deletes the last word
#.  a.append(")")            appends a closed bracket at the end of the list 
#.  w=" ".join(a)            joins words in the list by " "
#.  print w                  prints each line



**link to the code**
` link <https://github.com/elitalobo/HomeTask1/tree/master/mount>`_
