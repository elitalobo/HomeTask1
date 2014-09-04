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

