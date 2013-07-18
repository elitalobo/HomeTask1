#!/usr/bin/env python
import sys
import urllib2
class share_value(nasdaq_symbol):
    url = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1'% nasdaq_symbol
    sharevalue_file = urllib2.urlopen(url)
    print_sharevalue(sharevalue_file)

class print_share_value(value):
    sharevalue= value.read()
    print "Sharevalue of the company is (%s) " % sharevalue
    value.close()

if __name__ == '__main__' :
    if len(sys.argv)!==2:
        print " Invalid command "
        print " Enter the command in this format --> ./sharevalue.py <Nasdaq-Symbol> "  
    else:
       share_value(sys.argv[2])
    sys.exit(1)
    
    
