from lxml import html
import requests
import json
import cPickle as pickle
import time


#do not run this file otherwise lolking.net will be down
    
for num in range(7192,70000000):
    try:
        namelist=[]
        numlist=[]
        temp = str(num)
        page = requests.get('http://www.lolking.net/summoner/na/'+temp,timeout=0.5)
        tree = html.fromstring(page.text)
        lvl = tree.xpath('//div [@class="personal_ratings_lks"]/text()')
        time.sleep(0.2)
        
        if not lvl:
            pass
        else:
            print temp
            name = tree.xpath('//div[@id="summoner-titlebar-summoner-name"]/text()')
            namelist.append(name[0])
            numlist.append(num)
            with open('namefile.txt', 'a') as outfile:
                out_put= "{ \n"+"            " +json.dumps("name")+" : "+json.dumps(name[0]) +" , \n"
                outfile.write(out_put)
                out_put= "            " +json.dumps("number")+" : "+json.dumps(num) +" \n        }"
                outfile.write(out_put)
            
    except:
        pass


    