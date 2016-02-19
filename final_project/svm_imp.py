import math
import copy
from copy import deepcopy
def max(y,w,x,b):
    result = check_gradient(y, w, x, b)
    result = 1 - result
    if result >0:
        return result
    else:
        return 0

def check_gradient(y,w,x):

    temp=0
    for i in range(0,len(w)):
        temp= temp+w[i]*x[i]
    result = y*temp
    return result

def norm2(x):
    result =0
    for i in range(0 ,len(x)):
        result = result +x[i]*x[i]
    result=   math.sqrt(result)
    return result/len(x)

def minus(x,y):
    
    result =[]
    for i in range(0,len(x)):
        result.append(x[i]-y[i])
    return result
    
def svm_train(y_list,x_list,step,lda):  
    w=[]
    w_old=[]
    for i in range(0,len(x_list[0])):
        w.append(0)
        w_old.append(100)
    num=0

    while abs(norm2(minus(w,w_old))) > 0.001 and num< 1000:
        w_old=deepcopy(w)
        
        num=num+1
        
        for i in range(0,len(y_list)):
            y=y_list[i]
            x=x_list[i]
            if check_gradient(y, w, x) >1:
                
                w = list_minus(w, num_list(num_list(w,lda),step))
            else: 
                
                
                w= list_minus(w, num_list(list_minus(num_list(w,lda),num_list(x,y)),step))
                
   # print "turns for svm iteration:" +str(num)
    return w            
 
def num_list(x,y):
    result=[]
    for j in range(0,len(x)):
        result.append(x[j]*y)
    
    return result
def list_minus(x,w):
    result =[]
    for j in range(0,len(x)):
        result.append(x[j]-w[j])
    return result
    
def svm_predict(x,w): 
    temp =0     
    for i in range (0,len(x)):
        temp = temp+ x[i]*w[i]
    
    if temp > 0:
        return 1
    else:
        return -1
        