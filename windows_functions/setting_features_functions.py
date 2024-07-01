from PyQt5.QtWidgets import QMessageBox
from windows_functions.bubble_speech_functions import bubble44
from windows_functions.shared_variables import  timer44
from windows_functions.loading_windows import app, D3, D4, D44, D5, D55
from optional_features_functions.balanced_nutrition import Bilan_calculation, calculate_foodHealth
from optional_features_functions.Fitness_feature import fitness


#### calculate Fitness ####
def Fitness_result():
    age = D3.age.value()
    taille = D3.taille.value()
    poids = D3.poids.value()
    mince = D3.mince.isChecked()
    moyen = D3.moyen.isChecked()
    large = D3.large.isChecked()
    if age==0 or taille==0 or poids==0 or (mince==False and moyen ==False and large==False) :
        messageBox = QMessageBox() 
        messageBox.critical(None,"Error","You must complete all fields!")
        messageBox.setFixedSize(500,200);
    else: 
        IMC,PI = fitness(age, taille, poids, mince, moyen, large)
        D3.poidsid.display(PI)
        D3.indice.display(IMC)
###### calculate nutrition #####
def nutrition_result():
    lip, glu, prot = 0, 0, 0

    for i in range(27):
        if D4.fruit.item(i,0) is not None and D4.fruit.item(i,0).text() != "":
            fruit_item = D4.fruit.item(i,0).text()
            if int(fruit_item)!=0:
                a, b, c = calculate_foodHealth(fruit_item,i,"Fruits and Vegetables")
                lip, glu, prot = lip+a , glu+b , prot+c

    for i in range(7):
        if D4.drinks.item(i,0) is not None and D4.drinks.item(i,0).text() != "":
            drinks_item = D4.drinks.item(i,0).text()    
            if int(drinks_item)!=0:
                a, b, c = calculate_foodHealth(drinks_item,i,"Drinks and Diary Product")
                lip, glu, prot = lip+a , glu+b , prot+c
        
    for i in range(7):
        if D4.meat.item(i,0) is not None and D4.meat.item(i,0).text() != "":
            meat_item = D4.meat.item(i,0).text()
            if int(meat_item)!=0:
                a, b, c = calculate_foodHealth(meat_item,i,"Meats and Eggs")
                lip, glu, prot = lip+a , glu+b , prot+c
                
    for i in range(6):
        if D4.fish.item(i,0) is not None and D4.fish.item(i,0).text() != "":
            fish_item = D4.fish.item(i,0).text()
            if int(fish_item)!=0:
                a, b, c = calculate_foodHealth(fish_item,i,"Fish and products of sea")
                lip, glu, prot = lip+a , glu+b , prot+c

    for i in range(6):
        if D4.cereals.item(i,0) is not None and D4.cereals.item(i,0).text()  != "":
            cereals_item = D4.cereals.item(i,0).text()
            if int(cereals_item)!=0:
                a, b, c = calculate_foodHealth(cereals_item,i,"Cereals and Derivatives")
                lip, glu, prot = lip+a , glu+b , prot+c
                
    for i in range(4):
        if D4.sweets.item(i,0) is not None and D4.sweets.item(i,0).text() != "" :
            sweets_item = D4.sweets.item(i,0).text()
            if int(sweets_item)!=0:
                a, b, c = calculate_foodHealth(sweets_item,i,"Sweets")
                lip, glu, prot = lip+a , glu+b , prot+c
    if lip == 0 and glu == 0 and prot == 0:
        messageBox = QMessageBox() 
        messageBox.critical(None,"Error","You should enter at least one value! ")
        messageBox.setFixedSize(500,200);
    else:
        lip, glu, prot = Bilan_calculation(lip, glu, prot)
        D4.close()
        D44.show()
        global timer44
        D44.l1.setText("Thanks for")
        D44.l2.setText("the informations")
        timer44.timeout.connect(bubble44)
        timer44.start(5000)
        D44.Lipids.setValue(int(lip))
        D44.carb.setValue(int(glu))
        D44.proteins.setValue(int(prot))
        if prot<15 :
            D44.prot0.setText("Proteins in decrease")
            D44.prot1.setText("You should eat more Meat")
        elif prot>15:
            D44.prot0.setText("Proteins in excess")
            D44.prot1.setText("You should eat less Meat")
        else:
            D44.prot0.setText("Proteins balanced")
            D44.prot1.setText("Keep the same amount of Meat")
        if lip<25 :
            D44.lip0.setText("Lipids in decrease")
            D44.lip1.setText("You should eat more fruits and vegetables")
        elif lip>30:
            D44.lip0.setText("Lipids in excess")
            D44.lip1.setText("You should eat less fruits and vegetables")
        else:
            D44.lip0.setText("Lipids balanced")
            D44.lip1.setText("Keep the same amount of fruits and vegetables")
        if glu<55 :
            D44.glu0.setText("Carbohydrates in decrease")
            D44.glu1.setText("You should eat more sweets")
        elif glu>60:
            D44.glu0.setText("Carbohydrates in excess")
            D44.glu1.setText("You should eat less sweets")
        else:
            D44.glu0.setText("Carbohydrates balanced")
            D44.glu1.setText("Keep the same amount of Sweets")
