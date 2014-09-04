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


