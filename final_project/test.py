import prediction
from prediction import get_w,out_put_data

def main():
    
  
    for i in range (1,6):
        w=get_w('hero.json','game_info_test.json',0.2*i)

    
    

if __name__ == "__main__":
    main()