import os
from urllib import request
import re
import requests

#change path to test the script
path = "/Users/yinshangzhou/Desktop/scirpt/test"

os.chdir(path)


def removeDuplicates(mylist):
    mylist = list(dict.fromkeys(mylist))
    return mylist

#find the url in the string      
def findUrl(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]


def getcode(path):
    successR  = 0
    redirectM = 0
    clientE = 0
    serverE = 0
    for (root, dirs, files) in os.walk(path):
        for file in files:
            if '.DS_Store' in file:
                continue
            with open(os.path.join(root, file), "r") as auto:
                temp = auto.read()
                urlString = findUrl(temp)
                finalUrl = removeDuplicates(urlString)
                
                for url in finalUrl:
                    if (not url.startswith('http')) or url == 'https://www.wattsupmeters.com/secure/products.php?pn=0' or url == 'https://pax.grsecurity.net/docs/aslr.txt' or url == 'http://lenova.river-valley.com/svn/elsbst/trunk/New-Model-2/model2-names.bst':
                        continue
                    if(200 <= requests.get(url, headers = {"User-Agent": "Mozilla/5.0"}).status_code <= 299):
                        successR += 1

                    elif(300 <= requests.get(url, headers = {"User-Agent": "Mozilla/5.0"}).status_code <= 399):
                        redirectM += 1

                    elif(400 <= requests.get(url,headers = {"User-Agent": "Mozilla/5.0"}).status_code <= 499):
                        clientE += 1

                    elif(500 <= requests.get(url,headers = {"User-Agent": "Mozilla/5.0"}).status_code <= 599):
                        serverE += 1
    output(successR, redirectM, clientE, serverE)


def output(successR, redirectM, clientE, serverE):
    validity = (successR + redirectM) /(successR + redirectM + clientE + serverE) * 100
    print("Total link's STATUS")
    print("===================")
    print(str(successR) + " Success links")
    print(str(redirectM) + " Redirection links")
    print(str(clientE) + " Client error links")
    print(str(serverE) + " Server error links")
    print("Total link's validity: " + str(validity) + "%")
  
                
def main():

    getcode(path)

    
if __name__ == "__main__":
    main()                
               

            

    