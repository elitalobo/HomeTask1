==============
Planetparser
==============

Creating Virtualenv & installing BeautifulSoup4 
------------------------------------------------
Virtualenv is a tool to create isolated Python environments.It creates an environment that has its own installation directories, that doesn’t share libraries with other virtualenv environments.
Beautiful Soup is a Python library for pulling data out of HTML and XML files. The followings steps are to be followed for creating virtualenv and installing BeautifulSoup4 module in it.

::
    
   ~$ mkdir virtual
   ~$ cd virtual
   ~/virtual$ pip install virtualenv
   Requirement already satisfied (use --upgrade to upgrade): virtualenv in /usr/lib/python2.7/dist-packages
   Cleaning up...
   ~/virtual$ virtualenv vir1
   New python executable in vir1/bin/python
   Installing distribute..................................................................................................................... .   .......................................................................done.
   Installing pip...............done.
   ~/virtual$ source vir1/bin/activate
   (vir1)user@ubuntu:~/virtual$ pip install BeautifulSoup4
   Downloading/unpacking BeautifulSoup4
   Downloading beautifulsoup4-4.2.1.tar.gz (139Kb): 139Kb downloaded
   Running setup.py egg_info for package BeautifulSoup4
    
   Installing collected packages: BeautifulSoup4
   Running setup.py install for BeautifulSoup4
    
   Successfully installed BeautifulSoup4
   Cleaning up...

CODE DESCRIPTION
-----------------

**task**

The task was to create a virtualenv and write a file planetparser.py which when executed as ./planetparser.py would print the blog title and
author names from  http://planet.fedoraproject.org/. The required modules are to be installed in the virtualenv.

We use urllib2 module for opening the url and Beautifulsoup module for parsing through the webpage and retrieving required contents.

**link to the code**
`link <https://github.com/elitalobo/HomeTask1>`_

::
    
  CODE
  
  #!/usr/bin/env python 
  from bs4 import BeautifulSoup #imports BeautifulSoup package used for for parsing through the webpage  and retrieving required contents.
  import urllib2 # imports urllib2 required to open the webpage corresponding through the url passed to it.
  import sys

  def Planet_parser():
  url="http://planet.fedoraproject.org/" #url of the webpage to be scrapped.
  contents=urllib2.urlopen(url).read() #opens the url and reads its contents
  soup=BeautifulSoup(contents) #passes the contents to BeautifulSoup which returnsSoup object.
  soup.prettify() # represents the source page document as a nested data structure
  Author=soup.find_all('div', {'class':'blog-entry-author'}) # finds div tags belonging to class=blog-entry-author and stores it in Author as a  navigable strings.
  Title=soup.find_all('div',{'class':'blog-entry-title'}) #finds div tags belonging to class=blog-entry-title and stores itr in Title as         navigable strings. 
  count1= len(Author) # counts the no of div tags in Author
  count2= len(Title) #counts the no of div tags in Title
  i=0 #initialisation
  while i<count1:
     title1=BeautifulSoup(str(Title[i])) #passes the ith navigable string of Title to BeautifulSoup for parsing.
     author1= BeautifulSoup(str(Author[i])) #passes the ith navigable string of Author to BeautifulSoup for parsing.
     print "title of the blog :",title1.get_text() # prints title of the blog
     print "author of the blog:",author1.a.get_text() #prints author of the blog
     i=i+1 #incrementation

  if __name__ == '__main__':
  Planet_parser() #calls planet_parser function
  sys.exit(1) #exits





