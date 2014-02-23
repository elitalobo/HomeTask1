"""
convert into json files 

"""
import json
import sys
import requests
import argparse

def json_log(name,date,filename):
     item=open(filename,'r') 
     contents=item.read()
     item.close()
     mylogs=[]
     logs=({'name':name,'date':date,'contents':contents})
     mylogs.append({"logs":logs})
     fout=open("test.json",'w')
     fout.write( json.dumps(mylogs,indent=4))
     #json.dumps(mylogs,fout,indent=4)
     fout.close()
     fin=open("test.json",'r')
     s=fin.read()
     print s
     jsonobj=json.loads(s)
     print jsonobj
     #print type(s)
     #jsonobj=json.load(contents)
     #print jsonobj
     fin.close()

if __name__ == "__main__":
     
     args = argparse.ArgumentParser(description="Converts log files into json databases")
    
     args.add_argument("name", help = "Name of the log")
     args.add_argument("date", help = "Date of the log")
     args.add_argument("path", help = "Path/url of the log")
     json_log(sys.argv[1],sys.argv[2],sys.argv[3])
     
     
