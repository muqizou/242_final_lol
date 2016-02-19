class roles:
    def __init__(self,kda,rate,herocode):
        self.kdadict={}
        self.ratenumdict={}
        self.herocode=herocode
        self.sorted=[0,0,0,0,0]

        for i in range(0,len(herocode)):
            self.kdadict[herocode[i]]=kda[i]
            self.ratenumdict[herocode[i]]=rate[i]

        
    
     
    def print_info(self):
        print "top:"+str(self.sorted[0])+"kda: "+str(self.kdadict[str(self.sorted[0])])
        print "jun:"+str(self.sorted[1])+"kda: "+str(self.kdadict[str(self.sorted[1])])
        print "mid:"+str(self.sorted[2])+"kda: "+str(self.kdadict[str(self.sorted[2])])
        print "adc:"+str(self.sorted[3])+"kda: "+str(self.kdadict[str(self.sorted[3])])
        print "sup:"+str(self.sorted[4])+"kda: "+str(self.kdadict[str(self.sorted[4])])
        
    def get(self,role,herocode):
        if role == "top":
            self.sorted[0]=herocode
        elif role =="jun":
            self.sorted[1]=herocode
        elif role == "mid":
            self.sorted[2]=herocode
        elif role == "adc":
            self.sorted[3]= herocode
        elif role == "sup":
            self.sorted[4]= herocode
        else:
            print "ERROR in role"
        
    def out(self,role):        
        if role == "top" :
            return self.sorted[0]
        elif role =="jun":
            return self.sorted[1]
        elif role == "mid":
            return self.sorted[2]
        elif role == "adc":
            return self.sorted[3]
        elif role == "sup":
            return self.sorted[4]
        else:
            print "ERROR in role"