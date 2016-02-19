# -*- coding: UTF-8 -*-
from lxml import html
import requests
import json
import cPickle as pickle
import time
import xml.etree.ElementTree as ET

import datetime
import re


#this file is used to get game information by gamers' name on op.gg
with open('rest.json') as data_file:
    data= json.load(data_file)

for i in range(0,len(data["names"])):
    name=data["names"][i]["name"]
    #pick the name
    try:
        page = requests.get('https://na.op.gg/summoner/userName='+name,timeout=10)
        #I used https here instead of http, there may a warning out, but the requests are more possible to be successful
        tree = html.fromstring(page.text)
        optionlist = tree.xpath('//option/@value')
        namelist = tree.xpath('//option/text()')
        
        num_to_name_dict ={}
        name_to_num_dict = {}
        for i in range(1,len(optionlist)):
            num_to_name_dict[optionlist[i]]=namelist[i].encode("utf-8").strip()
            name_to_num_dict[namelist[i].encode("utf-8").strip()]=optionlist[i]
        datelist = tree.xpath('//span[@class = "TimeStamp"]/span/text()')
        #get the date of each game first
        today = datetime.datetime.today()
        dayrange=today-datetime.timedelta(days=7)
        #for here I will store the game happened in recent 7 days
        record=len(datelist)
        for i in range(0,len(datelist)):
            abletime=datelist[i]
            t=datetime.datetime.strptime(abletime,'%Y-%m-%d %H:%M:%S')
            if t<dayrange:
                record = i
                #if in the list his game is over 7 days the it will not be recorded
                break
            else:
                pass

        
        player_list=tree.xpath("//div[@class='SummonerName']/a/text()")
        
        player_hero_list=tree.xpath("//div[@class='ChampionImage']/div/@title")
        
        pass_check = True
        
        for i in range(1,record+1):

            typelist = tree.xpath('(//div[@class = "Title"]/h2[@class="Text"])['+str(i)+']/text()')
            
            if typelist[0].encode("utf-8").strip().replace(" ","").replace("\n","").replace("\t","") == '커스텀·':
                
                pass_check = False
            else:
                pass
            

        for i in range(1,record+1):

            typelist = tree.xpath('(//div[@class = "Title"]/h2[@class="Text"])['+str(i)+']/text()')

            if typelist[0].encode("utf-8").strip().replace(" ","").replace("\n","").replace("\t","") == '솔랭·' and pass_check == True:
                #this 솔랭 here means: Ranked solo
                bluelist=[]
                purplelist=[]
                blueplayerlist=[]
                purpleplayerlist=[]
                for j in range(0,5):
                    bluelist.append(name_to_num_dict[player_hero_list[(i-1)*10+j].encode("utf-8").strip()])
                    blueplayerlist.append(player_list[(i-1)*10+j])
                for j in range(5,10):
                    purplelist.append(name_to_num_dict[player_hero_list[(i-1)*10+j].encode("utf-8").strip()])
                    purpleplayerlist.append(player_list[(i-1)*10+j])
                
                #get the heros list for both blue and purple sides

                winorlost= tree.xpath("(//span [@class='GameResult'])/span/text()")
                inblue = False
                #for here if the user is in blue side, inblue will be true
                for i in range(0,len(blueplayerlist)):
                    if blueplayerlist[i] == name:
                        inblue = True
                    else:
                        pass
                    
                bluekdalist=[]
                blueratelist=[]
                for i in range(0,len(blueplayerlist)):
                    
                    new_name=blueplayerlist[i]
                    new_page = requests.get('https://na.op.gg/summoner/champions/userName='+new_name,timeout=10)
        #I used https here instead of http, there may a warning out, but the requests are more possible to be successful
                    new_tree = html.fromstring(new_page.text)
                    

                    klist=new_tree.xpath('//td[@class="Kill Cell"]/div/text()')
                    dlist=new_tree.xpath('//td[@class="Death Cell"]/div/text()')
                    alist=new_tree.xpath('//td[@class="Assist Cell"]/div/text()')
                    kdalist=[]
                    for j in range(0,len(klist)):
                        
                        try:
                            result=(float(klist[j])+float(alist[j]))/float(dlist[j])
                        except:
                            result=float(klist[j])+float(alist[j])
                        kdalist.append(result)
                        
                    ratelist = new_tree.xpath('//div [@class = "WinRatioGraph"]/span/text()')
                    
                    
                    
                    namelist = new_tree.xpath('//td [@class = "ChampionName Cell"]/text()')
                    result = -1
                                        
                    hero_name =  num_to_name_dict[str(bluelist[i])]
                    for i in range(0,len(namelist)):
                        if namelist[i].encode("utf-8").strip()== hero_name:
                            result=i
                            break
                    
                    
                    kda=kdalist[result]
                        
                    
                                
                             
                    try:
                        rate=re.findall("\d+",ratelist[result])[0]
                    except:
                        rate = -1
                    
                      
                         
                    blueratelist.append(rate)
                    bluekdalist.append(kda)
                   
                

                purplekdalist=[]
                purpleratelist=[]
                for i in range(0,len(purpleplayerlist)):
                    
                    new_name=purpleplayerlist[i]
                    new_page = requests.get('https://na.op.gg/summoner/champions/userName='+new_name,timeout=10)
        #I used https here instead of http, there may a warning out, but the requests are more possible to be successful
                    new_tree = html.fromstring(new_page.text)
                    

                    klist=new_tree.xpath('//td[@class="Kill Cell"]/div/text()')
                    dlist=new_tree.xpath('//td[@class="Death Cell"]/div/text()')
                    alist=new_tree.xpath('//td[@class="Assist Cell"]/div/text()')
                    kdalist=[]
                    for j in range(0,len(klist)):
                        try:
                            result=(float(klist[j])+float(alist[j]))/float(dlist[j])
                        except:
                            result=float(klist[j])+float(alist[j])
                        kdalist.append(result)
                        
                    ratelist = new_tree.xpath('//div [@class = "WinRatioGraph"]/span/text()')
                    
                    
                    
                    namelist = new_tree.xpath('//td [@class = "ChampionName Cell"]/text()')
                    result = -1
                                        
                    hero_name =  num_to_name_dict[str(purplelist[i])]
                    for i in range(0,len(namelist)):
                        if namelist[i].encode("utf-8").strip()== hero_name:
                            result=i
                            break
                    
                    kda=kdalist[result]

                    
                                
                             
                    try:
                        rate=re.findall("\d+",ratelist[result])[0]
                    except:
                        rate = -1
                    
                      
                          
                    purpleratelist.append(rate)
                    purplekdalist.append(kda)
                
                #we have whether the user is in blue side and whether he won, so we can define which side wins
                if (winorlost[0].encode("utf-8").strip()=="패배" and inblue ==False) or (winorlost[0].encode("utf-8").strip()=="승리" and inblue ==True):
                    win = "blue"
                else:
                    win = "purple"
                    
                #record the game information into files
                with open('game_info.txt', 'a') as outfile:
                        output="{\n "+"     " +json.dumps("win")+" : "+json.dumps(win)+",\n      "+json.dumps("name")+" : "+json.dumps(name)+",\n      "+json.dumps("blue")+":"+ json.dumps(bluelist)+",\n      "+json.dumps("purple")+":"+ json.dumps(purplelist)+",\n      "
                        output= output + json.dumps("bluekda")+" : "+json.dumps(bluekdalist)+",\n      "+json.dumps("purplekda")+" : "+json.dumps(purplekdalist)+",\n      "+json.dumps("bluerate")+" : "+json.dumps(blueratelist)+",\n      "+json.dumps("purplerate")+" : "+json.dumps(purpleratelist)
                        output= output + "\n},"
                        outfile.write(output)
        
    except:
        pass
    
