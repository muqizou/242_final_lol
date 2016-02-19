import roles
from roles import roles

class game_class:
    def __init__(self,blueside,purpleside,win):
        self.blueside=blueside
        self.purpleside=purpleside
        self.win=win
    
    def tell_result(self):
        return self.win
    
    def find_num(self,nums):
        for i in range(0,5):
            if nums[0] == self.blueside.herocode[i]:
                for j in range(0,5):
                    if nums[1] == self.purpleside.herocode[j]:
                        if self.win == "blue":
                            return "win"
                        else:
                            return "lose"
                    else:
                        pass
            else:
                pass
        for i in range(0,5):
            if nums[1] == self.blueside.herocode[i]:
                for j in range(0,5):
                    if nums[0] == self.purpleside.herocode[j]:
                        return "purple"
                    else:
                        pass
            else:
                pass
            
        return "NA"
            
            
    def print_info(self):
        self.blueside.print_info()
        self.purpleside.print_info()
        print self.win
    
