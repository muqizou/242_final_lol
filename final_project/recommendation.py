import prediction
from prediction import get_w,out_put_data
from lxml import html
import json
import requests
import xml.etree.ElementTree as ET
import re
from copy import deepcopy
def main():

    with open('hero.json') as hero_file:
        heros= json.load(hero_file)
        
    name="ahahahahahaha3"
   # name=raw_input("Enter Your name:\n")
   
    
    position=raw_input("Enter Your position:\n")
    
       
    while position.lower() != "top" and position.lower() != "mid" and position.lower() != "sup" and position.lower() != "adc" and position.lower() != "jun":
        print "Wrong position \n"
        position = raw_input("Enter Your position:\n")
    
    num_to_name_dict_eng={}
    for i in range(0,len(heros["heros"])):
        print "id: " + str(heros["heros"][i]["id"]) +"   name:" +str(heros["heros"][i]["name"])   
        num_to_name_dict_eng[heros["heros"][i]["id"]]=str(heros["heros"][i]["name"])
    hero_id=raw_input("Enter the opposite hero id:\n")
    
    print "CALCULATING..."
    data=out_put_data('hero.json','game_info_test.json')
    
    w=[3.4552641966265973, 2.2936115569936883, 2.8339761863531896, -0.65571474131581386, 0.67612770154302448, 0.0021561856300495795, 0.047894862771206172, -0.018026003280876991, 0.068755595358521659, 0.03423485270949745, 0.061151675387421063, 0.023609579514174712, 0.044585824851440789, 0.097702040023217987, -0.090243526364217827, -4.8637654976807321]

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
        new_page = requests.get('https://na.op.gg/summoner/champions/userName='+name.strip(),timeout=10)
        #I used https here instead of http, there may a warning out, but the requests are more possible to be successful
        new_tree = html.fromstring(new_page.text)

        
        temp=num_to_name_dict[hero_id]
        klist=new_tree.xpath('//td[@class="Kill Cell"]/div/text()')
        dlist=new_tree.xpath('//td[@class="Death Cell"]/div/text()')
        alist=new_tree.xpath('//td[@class="Assist Cell"]/div/text()')
        kdalist=[]
        for j in range(0,len(klist)):
                            
            if float(dlist[j]) != 0:
                result=(float(klist[j])+float(alist[j]))/float(dlist[j])
            else:
                result=float(klist[j])+float(alist[j])
            kdalist.append(result)
                            
        ratelist = new_tree.xpath('//div [@class = "WinRatioGraph"]/span/text()')
                        
           
                        
        namelist = new_tree.xpath('//td [@class = "ChampionName Cell"]/text()')
        for i in range(0,len(namelist)):
            namelist[i]=name_to_num_dict[namelist[i].encode("utf-8").strip()]
                
                
    
                                            
        for i in range(0,len(ratelist)):     
            try:
                rate=re.findall("\d+",ratelist[i])[0]
            except:
                rate = -1                    
            ratelist[i]=rate
                
        data_list=[] 
        w_factor=[]
        if position == "top":
             
            data_list=data.top_rate 
            w_factor.extend([w[0],3*w[5],3*w[10]])
        elif position == "mid":
            data_list=data.mid_rate
            w_factor.extend([w[1],3*w[6],3*w[11]])
        elif position == "jun":
            data_list == data.jun_rate
            w_factor.extend([w[2],2*w[7],2*w[12]])
        elif position == "adc":
            data_list == data.adc_rate
            w_factor.extend([w[3],w[8],w[13]])
        else:
            data_list == data.sup_rate
            w_factor.extend([w[4],1.5*w[9],1.5*w[14]])
          
         
        result_num=-1
        result=-1
        result_list=[]
        for i in range(0,len(namelist)):
            
            out=0
            temp=str(int(namelist[i]))+"#"+str(int(hero_id))
            sorted_str=sort_string(int(namelist[i]), int(hero_id))
            
            try:
                if temp == sorted_str and  isinstance(data_list[sorted_str], float):
                    out=w_factor[0]*data_list[sorted_str]
                    out= out +w_factor[1]*(float(kdalist[i])/2)+w_factor[2]*(float(ratelist[i])/50)
                    result_list.append(out)
                elif temp != sorted_str and isinstance(data_list[sorted_str], float):
                    
                    out=w_factor[0]*(1-data_list[sorted_str])
                    out= out +w_factor[1]*(float(kdalist[i])/2)+w_factor[2]*(float(ratelist[i])/50)
                    result_list.append(out)
                else:
                    
                    out= w_factor[1]*(float(kdalist[i])/2)+w_factor[2]*(float(ratelist[i])/50)
                    result_list.append(out)
                
                
            except:
                out = -1
                result_list.append(out)
                
            
            
            if result < out:
                result = out
                result_num=i
            else:
                pass
        
        
        tmp=list(result_list)
        result_list.sort()
        
        final_list=deepcopy(result_list[-5:])
        output=[]
        for i in range (0,5):
            output.append(tmp.index(final_list[4-i]))
        if result_num != -1:
            for i in range(0,5):
                print num_to_name_dict_eng[int(namelist[output[i]])]
        else:
            print "Data missed"
                    
                
                    
       
        
            
            
                    
                                
                             
                    
                       

    except:
        print "Connecting Error or Number Error"

def sort_string(num1,num2):
    if num1>  num2:
        return str(num2)+"#"+str(num1)
    else:
        return str(num1)+"#"+str(num2) 

if __name__ == "__main__":
    main()
