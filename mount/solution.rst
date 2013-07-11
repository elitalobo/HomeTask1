Mount
----------

**Task**
Write a file mount.py which when executed as ./mount.py gives the same output as mount command. For this we require to read /proc/mounts.

Code Description
--------------------

Basically we first open and read the mounts file in the proc directory which inturn is present in the root directory. By default the file content is not the same as output obtained by giving mount command on the CLI. So we need to assign the file contents to a variable and then manupulate it using basic python commands so as to achieve the desired output. 

The contents of the file which is read by a variable is first split into individual lines using f.split("\n"). Each line is  split into list of words using z[i].split(" "). Each list of words is then manupulated using insert() method , to insert words in the list, replace() method, to replace words or parts of words in the list, del() method, to delete words   from the list and append(), method to add words to the end of the list. Lastly we use join() method to join all the words in the list to form lines which is then printed as output. The /proc/mounts file is  closed at the end. 

**link to the code**
` link <https://github.com/elitalobo/HomeTask1/tree/master/mount>`_
