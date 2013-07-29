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

