from windows_functions.shared_variables import *
from windows_functions.loading_windows import  D1, D3, D4, D44, D5

########## Bubbles speech ##########

def bubble1():
    global index1, timer1
    index1+=1
    lD1a=["Hello! I am your","I am here","Do you suffer","To know your","Click on","Is your diet","Are you a","at the bottom"]
    lD1b=["virtual doctor","to help you","from any disease?","ideal weight...","your fitness ","balanced?","doctor?Look.. ","of the screen!"]
    D1.l1.setText(lD1a[index1])
    D1.l2.setText(lD1b[index1])
    timer1.start(5000)   
    if index1 == (len(lD1a)-1):
        index1=-1

def bubble3():
    global index3, timer3
    lD3a=["Enter your age,","Click on ","Find out your","Always protect","Feed","Do exercise","The perfect mind","Maintain your"]
    lD3b=["weight and height","calculate","ideal weight","yourself","well ","daily","in healthy body","ideal weight"]
    D3.l1.setText(lD3a[index3])
    D3.l2.setText(lD3b[index3])
    timer3.start(5000)
    index3+=1
    if index3 == (len(lD3a)-1):
        index3=-1

def bubble44():
    global index44, timer44 
    lD4a=["Is your diet","Check it out ","Your food safety","Enter your","I'm here to ","your health","Food must","Make sure your"]
    lD4b=["balanced?","immediately ","is your safety","food informations","take care of ...","","be healthy","food is healthy"]  
    D44.l1.setText(lD4a[index44])
    D44.l2.setText(lD4b[index44])
    timer44.start(5000)
    index44+=1
    if index44 == (len(lD4a)-1):
        index44=-1
def bubble4():
    global index4, timer4
    lD4a=["Is your diet","Check it out ","Your food safety","Enter your","I'm here to ","your health","Food must","Make sure your"]
    lD4b=["balanced?","immediately ","is your safety","food informations","take care of ...","","be healthy","food is healthy"]
    D4.l1.setText(lD4a[index4])
    D4.l2.setText(lD4b[index4])
    timer4.start(5000)
    index4+=1
    if index4 == (len(lD4a)-1):
        index4=-1

def bubble5():
    global index5, timer5
    lD5a=["Hello doctor!","Enter your","Share your","Your information","to our","We learn from","The developers","Thanks for"]
    lD5b=["","informations first","information with us","contributes..","development","your experiences","need your help","your contribution"]
    D5.l1.setText(lD5a[index5])
    D5.l2.setText(lD5b[index5])
    timer5.start(5000)
    index5+=1
    if index5 == (len(lD5a)-1):
        index5=-1
