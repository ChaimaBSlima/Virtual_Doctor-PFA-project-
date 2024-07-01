from PyQt5.QtWidgets import QApplication
from windows_functions.loading_windows import  D2D, D2Z, D2S, D2F
from Consultation_Ai_functions.shared_variables import *
from Health_Data.data_relation import*
from Consultation_Ai_functions.speech_recognition_functions import talk

def Ai_analyzing_resultZ(n,points):
    global  diseases, D2Z, D2S, D2F
    test = False
    for i in range(1,n):
        req = "select [Diseases ID], Diseases, Diseases_points, Medical_drugs, Medical_tests, doctor_name, speciality, phone, address from Diseases, [doctor log in] where [doctor log in].doctor_id = Diseases.doctor_id and Diseases.[Diseases ID] ="+str(diseases[i])
        cursor.execute(req)
        v=cursor.fetchall()
        if points == v[0][2] :
            test = True
            D2Z.close()
            D2S.show()
            D2S.dis.setText("You have " + (v[0][1]))
            D2S.drugs.setText("")
            D2S.speciality.setText("")
            D2S.doctor.setText("")
            D2S.phone.setText("")
            D2S.address.setText("")
            D2S.tests.setText("")
            QApplication.processEvents()
            talk("You have " + (v[0][1]))
            D2S.drugs.setText(v[0][3])
            QApplication.processEvents()
            talk("In the first column, I suggest some drugs to have for a week which are")
            talk(v[0][3])
            D2S.tests.setText(v[0][4])
            QApplication.processEvents()
            talk("If you didn't get well in a week make those medical tests mentioned in the second column")
            talk(v[0][4])
            D2S.speciality.setText("Then visit this  " + (v[0][6])+":")
            D2S.doctor.setText(v[0][5])
            D2S.phone.setText(str(v[0][7]))
            D2S.address.setText(v[0][8])
            QApplication.processEvents()
            talk("Then visit this  " + (v[0][6])+":")
            talk("Doctor "+v[0][5])
            talk("Office number is "+ str(v[0][7]))
            talk ("Address is " + v[0][8])
    if test == False:
        D2Z.close()
        D2F.show()
        D2F.doctor.setText("")
        D2F.phone.setText("")
        D2F.address.setText("")
        QApplication.processEvents()
        talk(D2F.text1.text())
        req = "SELECT  doctor_name, phone,address FROM [Doctor log in] WHERE doctor_id = 1"
        cursor.execute(req)
        v=cursor.fetchall()
        D2F.doctor.setText(v[0][0])
        D2F.phone.setText(str(v[0][1]))
        D2F.address.setText(v[0][2])
        QApplication.processEvents()
        talk("Doctor "+ D2F.doctor.text())
        talk("Office number is "+D2F.phone.text())
        talk ("Address is " + D2F.address.text())
        talk(D2F.text2.text())
        
def Ai_analyzing_resultD(n,points):
    global  diseases, D2D, D2S,D2F
    test = False
    for i in range(1,n):
        req = "select [Diseases ID], Diseases, Diseases_points, Medical_drugs, Medical_tests, doctor_name, speciality, phone, address from Diseases, [doctor log in] where [doctor log in].doctor_id = Diseases.doctor_id and Diseases.[Diseases ID] ="+str(diseases[i])
        cursor.execute(req)
        v=cursor.fetchall()
        if points == v[0][2] :
            D2D.close()
            D2S.show()
            test = True
            D2S.dis.setText("You have " + (v[0][1]))
            D2S.drugs.setText("")
            D2S.speciality.setText("")
            D2S.doctor.setText("")
            D2S.phone.setText("")
            D2S.address.setText("")
            D2S.tests.setText("")
            QApplication.processEvents()
            talk("You have " + (v[0][1]))
            D2S.drugs.setText(v[0][3])
            QApplication.processEvents()
            talk("In the first column, I suggest some drugs to have for a week which are")
            talk(v[0][3])
            D2S.tests.setText(v[0][4])
            QApplication.processEvents()
            talk("If you didn't get well in a week make those medical tests mentioned in the second column")
            talk(v[0][4])
            D2S.speciality.setText("Then visit this  " + (v[0][6])+":")
            D2S.doctor.setText(v[0][5])
            D2S.phone.setText(str(v[0][7]))
            D2S.address.setText(v[0][8])
            QApplication.processEvents()
            talk("Then visit this  " + (v[0][6])+":")
            talk("Doctor "+v[0][5])
            talk("Office number is "+ str(v[0][7]))
            talk ("Address is " + v[0][8])
    if test == False:
        D2D.close()
        D2F.show()
        D2F.doctor.setText("")
        D2F.phone.setText("")
        D2F.address.setText("")
        QApplication.processEvents()
        talk(D2F.text1.text())
        req = "SELECT  doctor_name, phone,address FROM [Doctor log in] WHERE doctor_id = 1"
        cursor.execute(req)
        v=cursor.fetchall()
        D2F.doctor.setText(v[0][0])
        D2F.phone.setText(str(v[0][1]))
        D2F.address.setText(v[0][2])
        QApplication.processEvents()
        talk("Doctor "+ D2F.doctor.text())
        talk("Office number is "+D2F.phone.text())
        talk ("Address is " + D2F.address.text())
        talk(D2F.text2.text())
    

