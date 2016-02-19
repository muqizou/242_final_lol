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
import position_check
from position_check import classify_heros
import calculation_set
from calculation_set import calculation_set
import random
from random import shuffle
import svm_imp
from svm_imp import svm_train,svm_predict 

def sort_string(num1,num2):
    if num1>  num2:
        return str(num2)+"#"+str(num1)
    else:
        return str(num1)+"#"+str(num2) 
 
def get_x(train_list,data):
    list_x=[]
    top_blue=train_list.blueside.sorted[0]
    top_purple=train_list.purpleside.sorted[0]  
    temp_string= str(top_blue)+"#"+str(top_purple)
    top_string=sort_string(top_blue, top_purple)
    if temp_string == top_string:
        list_x.append(data.top_rate[top_string])
    else:
        list_x.append(1-data.top_rate[top_string])
        
    jun_blue=train_list.blueside.sorted[1]
    jun_purple=train_list.purpleside.sorted[1]
    temp_string= str(jun_blue)+"#"+str(jun_purple)
    jun_string=sort_string(jun_blue, jun_purple)
    if temp_string == jun_string:
        list_x.append(data.jun_rate[jun_string])
    else:
        list_x.append(1-data.jun_rate[jun_string])
        

    mid_blue=train_list.blueside.sorted[2]
    mid_purple=train_list.purpleside.sorted[2]
    temp_string= str(mid_blue)+"#"+str(mid_purple)
    mid_string=sort_string(mid_blue,mid_purple)
    if temp_string == mid_string:
        list_x.append(data.mid_rate[mid_string])
    else:
        list_x.append(1-data.mid_rate[mid_string])
        
    adc_blue=train_list.blueside.sorted[3]
    adc_purple=train_list.purpleside.sorted[3]    
    
    temp_string= str(adc_blue)+"#"+str(adc_purple)
    adc_string=sort_string(adc_blue, adc_purple)
    if temp_string == adc_string:
        list_x.append(data.adc_rate[adc_string])
    else:
        list_x.append(1-data.adc_rate[adc_string])
            
    sup_blue=train_list.blueside.sorted[4]
    sup_purple=train_list.purpleside.sorted[4]    
    temp_string= str(sup_blue)+"#"+str(sup_purple)
    sup_string=sort_string(sup_blue, sup_purple)
    if temp_string == sup_string:
        list_x.append(data.sup_rate[sup_string])
    else:
        list_x.append(1-data.sup_rate[sup_string])
            

    try:
        top_kda=train_list.blueside.kdadict[str(top_blue)]/train_list.purpleside.kdadict[str(top_purple)]
        
    except:
        top_kda=2   
    list_x.append(top_kda)

    try:
        jun_kda=train_list.blueside.kdadict[str(jun_blue)]/train_list.purpleside.kdadict[str(jun_purple)]
        
    except:
        jun_kda=2   
    list_x.append(jun_kda)
    
    try:
        mid_kda=train_list.blueside.kdadict[str(mid_blue)]/train_list.purpleside.kdadict[str(mid_purple)]
        
    except:
        mid_kda=2   
    list_x.append(mid_kda)
    
    try:
        adc_kda=train_list.blueside.kdadict[str(adc_blue)]/train_list.purpleside.kdadict[str(adc_purple)]
        
    except:
        adc_kda=2   
    list_x.append(adc_kda)
    
    try:
        sup_kda=train_list.blueside.kdadict[str(sup_blue)]/train_list.purpleside.kdadict[str(sup_purple)]
              
    except:
        sup_kda=2
    list_x.append(adc_kda)    
    
    

    


    list_x.append(1)

    return list_x         
    
def get_y(train_list):
    if train_list.win == "blue":
        return 1
    else:
        return -1

def multi_two(w,x):
    result =0
    for i in range(0,len(w)):
        result = result+w[i]*x[i]
    
    return result

def main():
    with open('hero.json') as hero_file:
        heros= json.load(hero_file)
    
    with open('game_info.json') as game_file:
        game= json.load(game_file)
    
    
    data = calculation_set(heros)
    
   
    gamelist=classify_heros(game,heros,1)

    
    for i in range(0,len(gamelist)):
        data.add_info(gamelist[i])
        

    for i in range(0,3):
        iteration(data,gamelist)
    
    

        
    
def iteration(data,gamelist):
    shuffle_num = [i for i in range(len(gamelist))]
    shuffle(shuffle_num)

    train_list=[]
    test_list=[]
    
    for i in range (0,len(gamelist)):
        if i < int(0.8*len(gamelist)):
            train_list.append(gamelist[shuffle_num[i]])
        else:
            test_list.append(gamelist[shuffle_num[i]])
        

    
    train_y=[]
    train_x=[]
    for i in range(0,len(train_list)):
        train_y.append(get_y(train_list[i]))
        train_x.append(get_x(train_list[i],data))
        
    test_y=[]
    test_x=[]
    for i in range(0,len(test_list)):
        test_y.append(get_y(test_list[i]))
        test_x.append(get_x(test_list[i],data))
    
    w=svm_train(train_y,train_x,0.001,0.001)
    
    correct=0
    for i in range(0,len(train_list)):
        if train_y[i] == svm_predict(w,train_x[i]):
            
            correct=correct+1
        else:
            pass
        
    print correct/len(train_list)
    
    correct_test=0
    for i in range(0,len(test_list)):
        if test_y[i] == svm_predict(w,test_x[i]):
            correct_test=correct_test+1
        else:
            pass
        
    print correct_test/len(test_list)      
        
    
    
    print w
        
      
        
if __name__ == "__main__":
    main()
