#!/usr/bin/env python
import sys #import sys package
import urllib2 #import urllib2 package

def  share_value(nasdaq_symbol): #defines share_value function
    nasdaq_symbol.upper() #converts the nasdaq symbol to uppercase  if in lowercase
    url = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1'% nasdaq_symbol # url  for finding sharevalue
    sharevalue_file = urllib2.urlopen(url) # opens the webpage corresponding to the url
    print_sharevalue(sharevalue_file) #calls print_sharevalue function

def  print_sharevalue(value): #defines print_sharevalue function
    sharevalue1= value.read() #reads sharevalue file
    z=sharevalue1.split("\n") #splits the contents of the file into individual lines
    a=z[0].split(" ") # splits each line into words and stores it in a list
    
    if float(a[0])==0.0: #checks if sharevalue is zero
        print "Error:Invalid  NASDAQ symbol" # Since sharevalue cannot be zero
    else:
        print "Sharevalue of the company is %s " % sharevalue1 #prints sharevalue
    

if __name__ == '__main__': 
    if len(sys.argv)!=2: #checks if no of arguments  in the command is less than two
        print " Invalid command " #prints invalid command
        print " Enter the command in this format --> ./sharevalue.py <Nasdaq-Symbol> " # format of command
    else:
       share_value(sys.argv[1]) #calls share_value function
    sys.exit(1)
    
    
