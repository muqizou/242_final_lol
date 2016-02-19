from lxml import html
import requests
import json
import cPickle as pickle
import time
import xml.etree.ElementTree as ET




#this is the function for get users' name
for num in range(30001,40000):
    try:
        
        if num == 1000 or num == 10000 or num ==20000 or num==30000 or num==40000 or num == 50000 :
            print num
        else:
            pass

        temp= str(num)
        page = requests.get('http://www.lolsummoners.com/ladders/na/'+temp,timeout=2)
        print num
        tree = html.fromstring(page.text)
        namelist = tree.xpath("//tr [@class='ladder']/td [@class ='name']/a/text()")
        #I used four files to store the names, the main reason is it takes a long time to store all information
        with open('namefile4.txt', 'a') as outfile:
            for name in namelist:
                output="{ \n"+"            " +json.dumps("name")+" : "+json.dumps(name)+"\n},"
                outfile.write(output)
    
    except:
        pass

print "end"
