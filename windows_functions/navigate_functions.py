from PyQt5.QtWidgets import QApplication
from windows_functions.bubble_speech_functions import *
from windows_functions.home_buttoms_functions import *
from windows_functions.shared_variables import *
from windows_functions.loading_windows import *
from windows_functions.relation_AI_window import *
from Doctors_login_functions.doctor_login_functions import*
from windows_functions.main_window_function import mainwindow
from windows_functions.setting_features_functions import Fitness_result, nutrition_result

##### Leaving the app ####
def leave():
    D1.close()
########

##### clicking on the second bottom Fitness ####
def Fitness():
    global index3, timer3
    D1.close()
    D3.show()
    D3.age.setValue(0)
    D3.taille.setValue(0)
    D3.poids.setValue(0)
    D3.poidsid.display(0)
    D3.indice.display(0)
    QApplication.processEvents()
    timer3.timeout.connect(bubble3)
    timer3.start(10)

##### clicking on the First bottom consultation ####
def consultation():
    D1.close()
    D2.show()

##### clicking on the Third bottom balanced nutrition #####
def balance():
    global index4, timer4
    D1.close()
    D4.show()
    QApplication.processEvents()
    timer4.timeout.connect(bubble4)
    timer4.start(10)

##### clicking on the last bottom doctor  contribution #####
def doctor():
    global index5, timer5
    D1.close()
    D5.show()
    D5.username.setText("")
    D5.passwrd.setText("")
    D5.wrong.setText("")
    QApplication.processEvents()
    timer5.timeout.connect(bubble5)
    timer5.start(10)



def connection():
    mainwindow()
    D1.leave.clicked.connect(leave)
    D1.Fitness.clicked.connect(Fitness)
    D1.consultation.clicked.connect(consultation)
    D1.balance.clicked.connect(balance)
    D1.doctor.clicked.connect(doctor)
    ###home button connection###
    D2.home.clicked.connect(home2)
    D2D.home.clicked.connect(home2D)
    D2Z.home.clicked.connect(home2Z)
    D2S.home.clicked.connect(home2S)
    D2F.home.clicked.connect(home2F)
    D3.home.clicked.connect(home3)
    D4.home.clicked.connect(home4)
    D44.home.clicked.connect(home44)
    D5.home.clicked.connect(home5)
    D55.home.clicked.connect(home55)
    ###back button###
    D55C.back.clicked.connect(back)
    ###functional buttons###
    D2.zira.clicked.connect(zira)
    D2.david.clicked.connect(david)
    D4.calculate.clicked.connect(nutrition_result)
    D3.calculer.clicked.connect(Fitness_result)
    D5.ok.clicked.connect(doctor_login)
    D55.change.clicked.connect(doctor_change)
    D55.send.clicked.connect(mail_sent)
    D55C.change.clicked.connect(doctor_change)
    app.exec_()

