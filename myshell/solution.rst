============
Myshell
============

**task**

Write a code to create a cmd shell which greets the user on giving the command greet and which prints sharevalue of company on giving the 
command stock <NASDAQ_SYMBOL>.

**CODE**
This is the code of Myshell.py. It imports Stock function from ShareValue module.

::
   
   from cmd2 import Cmd
   __version__ = '0.1'
   from getpass import getuser
   import requests 
   import sys
   from ShareValue import Stock #imports Stock function from Sharevalue module
   # this code creates a cmd shell
   class Application(Cmd):
       """
       The main Application class
     
       """

       def __init__(self):
            Cmd.__init__(self)

       def do_hello(self,line):
            print "Hello:",line
            # prints hello <line> on giving the command hello <line>
            
       def do_sayit(self, line):
            print "Python Rocks!"
            # prints Pyhton Rocks! on giving the command sayit <line>
           
       def do_greet(self, line):
            print "Hi! %s" %(getuser()) # username is obtained by using requests library
            # greets user on giving the command greet

       def do_stock(self,line):
            Stock(line)
            # prints stock value on giving the command stock <NASDAQ_SYMBOL>
       def main():
            app = Application() #calls Application() function
            app.cmdloop()


   if __name__ == '__main__':
           main() #calls main()

**code for ShareValue.py**

::
   
   import requests
   #imports request library

   def Stock(line1): #defines stock function
        a=line1.split(" ") #splits input line
        url = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1'% a[0]
        sharevalue=requests.get(url) # uses request library to open url
        s=sharevalue.text #obtains text contents from webpage
        c=str(s).split("\n") #splits contents into individual lines
        d= c[0].split(" ") #splits first line into words
        if str(d[0])=="0.00\r": #checks if nasdaq symbol is invalid by checking if sharevalue=0
           print "invalid nasdaq symbol" #prints invalid nasdaq symbol
        else: #else prints sharevalue of the company
           print "Sharevalue of the company with nasdaq symbol %s is %s" %(a[0],sharevalue.text)
        sharevalue.close()

**link**
`link <https://github.com/elitalobo/HomeTask1>`_
