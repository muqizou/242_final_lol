from __future__ import division
class calculation_set:
    def __init__(self,heros):
        self.top_up=self.find_combination(heros, "top")
        self.mid_up=self.find_combination(heros, "mid")
        self.jun_up=self.find_combination(heros, "jun")
        self.adc_up=self.find_combination(heros, "adc")
        self.sup_up=self.find_combination(heros, "sup")
        self.top_down=self.find_combination(heros, "top")
        self.mid_down=self.find_combination(heros, "mid")
        self.adc_down=self.find_combination(heros, "adc")
        self.sup_down=self.find_combination(heros, "sup")
        self.jun_down=self.find_combination(heros, "jun")
        self.top_rate=self.find_combination(heros, "top")
        self.mid_rate=self.find_combination(heros, "mid")
        self.jun_rate=self.find_combination(heros, "jun")
        self.sup_rate=self.find_combination(heros, "sup")
        self.adc_rate=self.find_combination(heros, "adc")
        
        self.top_single_up=self.set_single(heros, "top")
        self.mid_single_up=self.set_single(heros, "mid")
        self.jun_single_up=self.set_single(heros, "jun")
        self.adc_single_up=self.set_single(heros, "adc")
        self.sup_single_up=self.set_single(heros, "sup")
        self.top_single_down=self.set_single(heros, "top")
        self.mid_single_down=self.set_single(heros, "mid")
        self.jun_single_down=self.set_single(heros, "jun")
        self.adc_single_down=self.set_single(heros, "adc")
        self.sup_single_down=self.set_single(heros, "sup")
        self.top_single_rate=self.set_single(heros, "top")
        self.mid_single_rate=self.set_single(heros, "mid")
        self.jun_single_rate=self.set_single(heros, "jun")
        self.adc_single_rate=self.set_single(heros, "adc")
        self.sup_single_rate=self.set_single(heros, "sup")
        
        self.mid_jun_up=self.set_double(heros, "mid", "jun")
        self.mid_jun_down=self.set_double(heros, "mid", "jun")
        self.mid_jun_rate=self.set_double(heros, "mid", "jun")
        
        self.adc_sup_up=self.set_double(heros, "adc", "sup")
        self.adc_sup_down=self.set_double(heros, "adc", "sup")
        self.adc_sup_rate=self.set_double(heros, "adc", "sup")
        
        self.total_blue_win=0
        self.total_purple_win=0
        self.total_rate=0
        
        
        
    def set_single(self,heros,position):
        position_set=[]
        for i in range(0,len(heros["heros"])):
            for j in range(0,len(heros["heros"][i]["position"])):
                if heros["heros"][i]["position"][j] == position:
                    position_set.append(heros["heros"][i]["id"])
                else:
                    pass
        position_set= sorted(position_set)
        result_set={}
        for i in range(0,len(position_set)):
            result_set[position_set[i]]=0
         
        return result_set
    
    
    def set_double(self,heros,position1,position2):
        position1_set=[]   
        position2_set=[]
        for i in range(0,len(heros["heros"])):
            for j in range(0,len(heros["heros"][i]["position"])):
                if heros["heros"][i]["position"][j] == position2:
                    position2_set.append(heros["heros"][i]["id"])
                else:
                    pass
                if heros["heros"][i]["position"][j] == position1:
                    position1_set.append(heros["heros"][i]["id"])
                else:
                    pass
        position1_set= sorted(position1_set)
        position2_set =sorted(position2_set)
        result_set={}
        for i in range(0,len(position1_set)):
              for j in range(0,len(position2_set)):
                  if position1_set[i] != position2_set[j]:
                      result=str(position1_set[i])+"#"+str(position2_set[j])
                      result_set[result]=0
    
        return result_set  
        
        
        
    def find_combination(self,heros,position):
        position_set=[]
        for i in range(0,len(heros["heros"])):
            for j in range(0,len(heros["heros"][i]["position"])):
                if heros["heros"][i]["position"][j] == position:
                    position_set.append(heros["heros"][i]["id"])
                else:
                    pass
        position_set= sorted(position_set)
        result_set={}
        for i in range(0,len(position_set)):
              for j in range(i+1,len(position_set)):
                  result=str(position_set[i])+"#"+str(position_set[j])
                  result_set[result]=0
    
        return result_set  
    
    
    def add_info(self,game):
        win=game.win
        blueside=game.blueside
        purpleside=game.purpleside
        
        temp_blue_bot=str(blueside.sorted[3])+"#"+str(blueside.sorted[4])
        temp_purple_bot=str(purpleside.sorted[3])+"#"+str(purpleside.sorted[4])
        temp_blue_up=str(blueside.sorted[2])+"#"+str(blueside.sorted[1])
        temp_purple_up=str(purpleside.sorted[2])+"#"+str(purpleside.sorted[1])
        
        if (win == "blue"):
            self.total_blue_win=self.total_blue_win+1
            self.top_single_up[blueside.sorted[0]]=self.top_single_up[blueside.sorted[0]] +1
            self.jun_single_up[blueside.sorted[1]]=self.jun_single_up[blueside.sorted[1]] +1
            self.mid_single_up[blueside.sorted[2]]=self.mid_single_up[blueside.sorted[2]] +1
            self.adc_single_up[blueside.sorted[3]]=self.adc_single_up[blueside.sorted[3]] +1
            self.sup_single_up[blueside.sorted[4]]=self.sup_single_up[blueside.sorted[4]] +1
            self.mid_jun_up[temp_blue_up]=self.mid_jun_up[temp_blue_up]+1
            self.adc_sup_up[temp_blue_bot]=self.adc_sup_up[temp_blue_bot]+1
            self.adc_sup_down[temp_purple_bot]=self.adc_sup_down[temp_purple_bot]+1
            self.mid_jun_down[temp_purple_up]=self.mid_jun_down[temp_purple_up]+1
            self.top_single_down[purpleside.sorted[0]]=self.top_single_down[purpleside.sorted[0]] +1
            self.jun_single_down[purpleside.sorted[1]]=self.jun_single_down[purpleside.sorted[1]] +1
            self.mid_single_down[purpleside.sorted[2]]=self.mid_single_down[purpleside.sorted[2]] +1
            self.adc_single_down[purpleside.sorted[3]]=self.adc_single_down[purpleside.sorted[3]] +1
            self.sup_single_down[purpleside.sorted[4]]=self.sup_single_down[purpleside.sorted[4]] +1
            
        else:
            self.total_purple_win=self.total_purple_win+1
            self.top_single_up[purpleside.sorted[0]]=self.top_single_up[purpleside.sorted[0]] +1
            self.jun_single_up[purpleside.sorted[1]]=self.jun_single_up[purpleside.sorted[1]] +1
            self.mid_single_up[purpleside.sorted[2]]=self.mid_single_up[purpleside.sorted[2]] +1
            self.adc_single_up[purpleside.sorted[3]]=self.adc_single_up[purpleside.sorted[3]] +1
            self.sup_single_up[purpleside.sorted[4]]=self.sup_single_up[purpleside.sorted[4]] +1
            self.mid_jun_down[temp_blue_up]=self.mid_jun_down[temp_blue_up]+1
            self.adc_sup_down[temp_blue_bot]=self.adc_sup_down[temp_blue_bot]+1
            self.adc_sup_up[temp_purple_bot]=self.adc_sup_up[temp_purple_bot]+1
            self.mid_jun_up[temp_purple_up]=self.mid_jun_up[temp_purple_up]+1
            
            
            self.top_single_down[blueside.sorted[0]]=self.top_single_down[blueside.sorted[0]] +1
            self.jun_single_down[blueside.sorted[1]]=self.jun_single_down[blueside.sorted[1]] +1
            self.mid_single_down[blueside.sorted[2]]=self.mid_single_down[blueside.sorted[2]] +1
            self.adc_single_down[blueside.sorted[3]]=self.adc_single_down[blueside.sorted[3]] +1
            self.sup_single_down[blueside.sorted[4]]=self.sup_single_down[blueside.sorted[4]] +1
            
        self.mid_jun_rate[temp_blue_up]=self.mid_jun_up[temp_blue_up]/(self.mid_jun_up[temp_blue_up]+self.mid_jun_down[temp_blue_up])
        self.mid_jun_rate[temp_purple_up]=self.mid_jun_up[temp_purple_up]/(self.mid_jun_up[temp_purple_up]+self.mid_jun_down[temp_purple_up])
        self.adc_sup_rate[temp_blue_bot]=self.adc_sup_up[temp_blue_bot]/(self.adc_sup_up[temp_blue_bot]+self.adc_sup_down[temp_blue_bot])
        self.adc_sup_rate[temp_purple_bot]= self.adc_sup_up[temp_purple_bot]/(self.adc_sup_up[temp_purple_bot]+self.adc_sup_down[temp_purple_bot])
        
        self.total_rate=self.total_blue_win/(self.total_purple_win+self.total_blue_win)
        self.top_single_rate[purpleside.sorted[0]]=self.top_single_up[purpleside.sorted[0]]/(self.top_single_up[purpleside.sorted[0]]+self.top_single_down[purpleside.sorted[0]])
        self.jun_single_rate[purpleside.sorted[1]]=self.jun_single_up[purpleside.sorted[1]]/(self.jun_single_up[purpleside.sorted[1]]+self.jun_single_down[purpleside.sorted[1]])
        self.mid_single_rate[purpleside.sorted[2]]=self.mid_single_up[purpleside.sorted[2]]/(self.mid_single_up[purpleside.sorted[2]]+self.mid_single_down[purpleside.sorted[2]])
        self.adc_single_rate[purpleside.sorted[3]]=self.adc_single_up[purpleside.sorted[3]]/(self.adc_single_up[purpleside.sorted[3]]+self.adc_single_down[purpleside.sorted[3]])
        self.sup_single_rate[purpleside.sorted[4]]=self.sup_single_up[purpleside.sorted[4]]/(self.sup_single_up[purpleside.sorted[4]]+self.sup_single_down[purpleside.sorted[4]])
        self.top_single_rate[blueside.sorted[0]]=self.top_single_up[blueside.sorted[0]]/(self.top_single_up[blueside.sorted[0]]+self.top_single_down[blueside.sorted[0]])
        self.jun_single_rate[blueside.sorted[1]]=self.jun_single_up[blueside.sorted[1]]/(self.jun_single_up[blueside.sorted[1]]+self.jun_single_down[blueside.sorted[1]])
        self.mid_single_rate[blueside.sorted[2]]=self.mid_single_up[blueside.sorted[2]]/(self.mid_single_up[blueside.sorted[2]]+self.mid_single_down[blueside.sorted[2]])
        self.adc_single_rate[blueside.sorted[3]]=self.adc_single_up[blueside.sorted[3]]/(self.adc_single_up[blueside.sorted[3]]+self.adc_single_down[blueside.sorted[3]])
        self.sup_single_rate[blueside.sorted[4]]=self.sup_single_up[blueside.sorted[4]]/(self.sup_single_up[blueside.sorted[4]]+self.sup_single_down[blueside.sorted[4]])               
            
                
        
        
        temp=str(blueside.sorted[0])+"#"+str(purpleside.sorted[0])
        top=self.sort_string(blueside.sorted[0], purpleside.sorted[0])
        if (win == "blue" and top == temp) or (win =="purple" and top !=temp):
            self.top_up[top]=self.top_up[top]+1
            self.top_rate[top]=self.top_up[top] /(self.top_up[top]+self.top_down[top])
        else:
            self.top_down[top]=self.top_down[top]+1
            self.top_rate[top]=self.top_up[top] /(self.top_up[top]+self.top_down[top])            
        
        temp=str(blueside.sorted[1])+"#"+str(purpleside.sorted[1])
        jun=self.sort_string(blueside.sorted[1], purpleside.sorted[1])
        if (win == "blue" and jun == temp) or (win =="purple" and jun !=temp):
            self.jun_up[jun]=self.jun_up[jun]+1
            self.jun_rate[jun]=self.jun_up[jun] /(self.jun_up[jun]+self.jun_down[jun])
        else:
            self.jun_down[jun]=self.jun_down[jun]+1 
            self.jun_rate[jun]=self.jun_up[jun] /(self.jun_up[jun]+self.jun_down[jun])   
        
        temp=str(blueside.sorted[2])+"#"+str(purpleside.sorted[2])
        mid=self.sort_string(blueside.sorted[2], purpleside.sorted[2])
        if (win == "blue" and mid == temp) or (win =="purple" and mid !=temp):
            self.mid_up[mid]=self.mid_up[mid]+1
            self.mid_rate[mid]=self.mid_up[mid] /(self.mid_up[mid]+self.mid_down[mid])
        else:
            self.mid_down[mid]=self.mid_down[mid]+1
            self.mid_rate[mid]=self.mid_up[mid] /(self.mid_up[mid]+self.mid_down[mid])
            
        temp=str(blueside.sorted[3])+"#"+str(purpleside.sorted[3])            
        adc=self.sort_string(blueside.sorted[3], purpleside.sorted[3])
        if (win == "blue" and adc == temp) or (win =="purple" and adc !=temp):
            self.adc_up[adc]=self.adc_up[adc]+1
            self.adc_rate[adc]=self.adc_up[adc] /(self.adc_up[adc]+self.adc_down[adc])
        else:
            self.adc_down[adc]=self.adc_down[adc]+1
            self.adc_rate[adc]=self.adc_up[adc] /(self.adc_up[adc]+self.adc_down[adc])
         
        temp=str(blueside.sorted[4])+"#"+str(purpleside.sorted[4])            
        sup=self.sort_string(blueside.sorted[4], purpleside.sorted[4])
        if (win == "blue" and sup == temp) or (win =="purple" and sup !=temp):
            self.sup_up[sup]=self.sup_up[sup]+1
            self.sup_rate[sup]=self.sup_up[sup] /(self.sup_up[sup]+self.sup_down[sup])
        else:
            self.sup_down[sup]=self.sup_down[sup]+1
            self.sup_rate[sup]=self.sup_up[sup] /(self.sup_up[sup]+self.sup_down[sup])

             
    def sort_string(self,num1,num2):
        if num1>  num2:
            return str(num2)+"#"+str(num1)
        else:
            return str(num1)+"#"+str(num2) 