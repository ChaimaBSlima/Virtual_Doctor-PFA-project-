from PyQt5.QtWidgets import QMessageBox
from windows_functions.loading_windows import app, D55C

def phone_error():
            messageBox = QMessageBox() 
            messageBox.critical(None,"Error","Please enter a valid phone number with 8 numbers!")
            messageBox.setFixedSize(500,200);
            D55C.newphone.clear()

def address_error():
            messageBox = QMessageBox() 
            messageBox.critical(None,"Error","Please enter a valid address with location and number of km!")
            messageBox.setFixedSize(500,200);
            D55C.newaddress .clear()

def username_error(text):
            messageBox = QMessageBox() 
            messageBox.critical(None,"Error", text)
            messageBox.setFixedSize(500,200);
            D55C.newusername .clear()

def password_error():
            messageBox = QMessageBox() 
            messageBox.critical(None,"Error","Passowrd must at least have 6 letters!")
            messageBox.setFixedSize(500,200);
            D55C.newpass.clear()

def mail_error(text):
            messageBox = QMessageBox() 
            messageBox.critical(None,"Error",text)
            messageBox.setFixedSize(500,200);
            D55C.newpass.clear()
    