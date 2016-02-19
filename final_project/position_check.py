# -*- coding: UTF-8 -*-
from __future__ import division
from lxml import html
import requests
import json
import cPickle as pickle
import time
import xml.etree.ElementTree as ET
import roles
import game_class
from game_class import game_class
from roles import roles
import datetime
from collections import defaultdict
import code
from lxml.html.builder import CODE



def check_rate(data):
    bluewin=0
    for i in range(0,len(data["games"])):
        if data["games"][i]["win"] == "blue":
            bluewin=bluewin+1
        else:
            pass
        
    bluerate= bluewin/(len(data["games"]))*100
    print bluerate 
    return bluerate  


def get_hero(heros):
    herohash={}
    for i in range(0,len(heros["heros"])):
        herohash[heros["heros"][i]["id"]]=heros["heros"][i]["position"]
    
    return herohash

def get_name(heros):
    herohash={}
    for i in range(0,len(heros["heros"])):
        herohash[heros["heros"][i]["id"]]=heros["heros"][i]["name"]
    
    return herohash

def check_name(blueside,purpleside):
    for i in range(0,5):
        for j in range(0,5):
            if int(blueside[i]) == int(purpleside[j]):
                return False
            else:
                pass

    
def check_position_fill(herohash,blueside,purpleside,namelist,name):
    blueset=set()
    purpleset=set()
    
    for i in range(0,len(namelist)):
        if name == namelist[i]:
            return False
        else:
            pass
    
    for i in range(0,5):
        codepurple = int(purpleside[i])
        codeblue = int(blueside[i])
        bluelist=herohash[codeblue]
        purplelist= herohash[codepurple]
        purpleset.add(purplelist[0])
        blueset.add(bluelist[0])
        try:
            purpleset.add(purplelist[1])
        except:
            pass
        try:
            blueset.add(bluelist[1])
        except:
            pass
        try:
            purpleset.add(purplelist[2])
        except:
            pass
        try:
            blueset.add(bluelist[2])
        except:
            pass
    
    if (len(blueset) != 5 or len(purpleset) != 5):
        return False
    return True  

def divide_into_group(herohash,side,heroname):
    waitlist={}
    resultlist={}
    rolelist= [u"mid", u"top",u"jun",u"adc",u"sup"]

    
    for j in range(0,5):
        code = int(side[j])
        
        num_list= herohash[code]
        
        for i in range (0, len(num_list)):
            try:
                list=waitlist[num_list[i]]
            except:
                list=[]   
            list.append(code)
            waitlist[num_list[i]]=list
            
        if len(num_list) == 1:
            resultlist[num_list[0]] = code
            waitlist=remove_from_waitlist(waitlist,code)
        else:
            pass
       
    for j in range(0,5):
        code = rolelist[j]
        num_list= waitlist[code]
        try:
            temp = resultlist[code]
        except:
            if len(num_list) == 1:
                resultlist[code] = num_list[0]
                waitlist=remove_from_waitlist(waitlist,num_list[0])
            else:
                pass
    
    
    for j in range(0,5):
        for i in range(0,5):
            checkrole= rolelist[i]
            try:
                temp= resultlist[checkrole]
            except:
                try:
                    num_list = waitlist[checkrole] 
                    if len(num_list) == 1:
                        resultlist[checkrole] = num_list[0]
                        waitlist=remove_from_waitlist(waitlist,num_list[0])
                    else:
                        pass
                except:
                    pass
    
    for k in range(0,5):
        for j in range(0,5):
            try: 
                temp=resultlist[rolelist[j]]
            except:
                try:
                    temp=waitlist[rolelist[j]][0]
                    resultlist[rolelist[j]]=temp
                    waitlist=remove_from_waitlist(waitlist,temp)
                except:
                    
                    return {}
                
    
    return resultlist

def num_to_name (list,herohash):
    result_list=[]
    for i in range(0,5):
        hero=herohash[int(list[i])]
        result_list.append(hero)
    return result_list
    
def remove_from_waitlist(waitlist,num):
    rolelist= [u"adc",u"sup",u"jun",u"top",u"mid"]
    for j in range(0,5):
        
        try:
            check_list = waitlist[rolelist[j]]
        except:
            check_list = []
            
        try:
            check_list.remove(num)
        except:
            pass
        waitlist[rolelist[j]] = check_list
        
    return waitlist
    


def classify_heros(data,heros,factor):     
    herohash=get_hero(heros)
    heroname=get_name(heros)
    gamelist=[]
    mistakes =0
    problem =0
    gamelist=[]
    namelist=[]
    
    for i in range (0,int(len(data["games"])*factor)):
        checkname= check_name(data["games"][i]["blue"], data["games"][i]["purple"])
        if checkname == False:
            namelist.append(data["games"][i]["name"])
    

    for i in range(0,int(len(data["games"])*factor)):
        check= check_position_fill(herohash,data["games"][i]["blue"],data["games"][i]["purple"],namelist,data["games"][i]["name"])

        if check == False:
            mistakes=mistakes+1
        else:
            purplerole=roles(data["games"][i]["purplekda"],data["games"][i]["purplerate"],data["games"][i]["purple"])
            bluerole=roles(data["games"][i]["bluekda"],data["games"][i]["bluerate"],data["games"][i]["blue"])
            blue_list=divide_into_group(herohash,data["games"][i]["blue"],heroname)
            purple_list= divide_into_group(herohash,data["games"][i]["purple"],heroname)
            
            if(len(blue_list) == 0 or len(purple_list) == 0):
                problem= problem +1
            else:
                insert_to_class(purplerole, purple_list)
                insert_to_class(bluerole, blue_list)
                game=game_class(bluerole,purplerole,data["games"][i]["win"])
                gamelist.append(game)
                pass
    print "Data cannot be classified:"+str(problem)  
    print "Data error:"+str(mistakes)
    print "Total error:"+str(mistakes+problem)
    print "Total data:"+str(int(len(data["games"])*factor))
    return gamelist
    
    
def insert_to_class(role,list):
    role.get("top",list["top"])
    role.get("mid",list["mid"])
    role.get("jun",list["jun"])
    role.get("adc",list["adc"])
    role.get("sup",list["sup"])


    
    
    

