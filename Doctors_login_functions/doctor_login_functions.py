from windows_functions.loading_windows import D5, D55, D55C
from Doctors_login_functions.errors_functions import*
from Doctors_login_functions.mail_sent_function import*
from Health_Data.data_relation import*

def contains_number(s):
    return any(char.isdigit() for char in s)

def doctor_login():
    global  username, password
    req = "SELECT doctor_username, doctor_password, doctor_name, speciality, phone,address, doctor_id FROM [Doctor log in] WHERE doctor_username = ? AND doctor_password = ?"
    username = D5.username.text()
    password = D5.passwrd.text()
    cursor.execute(req, (username, password))
    v=cursor.fetchall()
    if not v:
        D5.wrong.setText("user name or password wrong")
    else:
        text = ""
        doctorId= v[0][6]
        D5.close()
        D55.show()
        D55.hello.setText("Hello Doctor " + v[0][2] + " !")
        D55.doctor.setText(v[0][2])
        D55.speciality.setText(v[0][3])
        D55.phone.setText(str(v[0][4]))
        D55.address.setText(v[0][5])
        D55.username.setText(v[0][0])
        D55.password.setText("*"*len(v[0][1]))
        D55.subject.clear()
        D55.mail.clear()
        D55.success.setText("")
        for i in range(11):
            req1 = "select  Diseases from Diseases where doctor_id = "+str(doctorId)+"and Diseases.[Diseases ID] ="+str(i)
            cursor.execute(req1)
            v1=cursor.fetchall()
            if v1:
                text = text + v1[0][0] + "\n"
        D55.diseases.setText(text) 
def   doctor_change():
    global username, password
    D55.close()
    D55C.show()
    test = False
    req = "SELECT doctor_username, doctor_password, doctor_name, speciality, phone,address FROM [Doctor log in] WHERE doctor_username = ? AND doctor_password = ?"
    cursor.execute(req, (username, password))
    v=cursor.fetchall()
    D55C.success.setText("")
    D55C.hello.setText("Hello Doctor " + v[0][2] + " !")
    D55C.doctor.setText(v[0][2])
    D55C.speciality.setText(v[0][3])
    D55C.phone.setText(str(v[0][4]))
    D55C.address.setText(v[0][5])
    D55C.username.setText(v[0][0])
    D55C.password.setText("*"*len(v[0][1]))
    new_pass = D55C.newpass.text()
    new_username = D55C.newusername.text()
    new_phone = D55C.newphone.text()
    new_address = D55C.newaddress.text()
    if new_phone != "":
        if new_phone.isnumeric() == False or len(new_phone) != 8:
                test = True
                phone_error()
                new_phone = D55C.newphone.text()
    if new_address  != "":
        if new_address .isnumeric() == True or contains_number(new_address ) == False or len(new_address ) < 8:
            test = True
            address_error()
            new_address = D55C.newaddress.text()
    if new_username  != "":
        if new_username.isalnum() == True:
            for i in range(1,9):
                query = "SELECT doctor_username FROM [Doctor log in] WHERE doctor_id =" + str(i)
                cursor.execute(query)
                T=cursor.fetchall()
                if new_username == T[0][0]:
                    test = True
                    username_error("Username exist already!")
                    new_username = D55C.newaddress.text()
                    break
        else:
            test = True
            username_error("Username must contain only letters and numbers!")
            new_username = D55C.newaddress.text()            
    if new_pass != "" :
        if len(new_pass) < 6 :
            test = True
            password_error()
            new_pass = D55C.newpass.text()
    if test == False:
        if new_phone != "":
            update_req = "UPDATE [Doctor log in] SET phone = ? WHERE doctor_username = ? and doctor_password = ?"
            cursor.execute(update_req, (new_phone, username, password))
            cnn.commit()
            D55C.success.setText("fields changed successfully !")
        if new_address  != "":
            update_req = "UPDATE [Doctor log in] SET address = ? WHERE doctor_username = ? and doctor_password = ?"
            cursor.execute(update_req, (new_address, username, password))
            cnn.commit()
            D55C.success.setText("fields changed successfully !")
        
        if new_username != "":
            update_req = "UPDATE [Doctor log in] SET doctor_username = ? WHERE doctor_username = ? and doctor_password = ?"
            cursor.execute(update_req, (new_username, username, password))
            cnn.commit()
            username = new_username
            D55C.success.setText("fields changed successfully !")

        if new_pass != "":
            update_req = "UPDATE [Doctor log in] SET doctor_password = ? WHERE doctor_username = ? and doctor_password = ?"
            cursor.execute(update_req, (new_pass, username, password))
            cnn.commit()
            password = new_pass
            D55C.success.setText("fields changed successfully !")
        
        req = "SELECT doctor_username, doctor_password, phone,address FROM [Doctor log in] WHERE doctor_username = ? AND doctor_password = ?"
        cursor.execute(req, (username, password))
        v=cursor.fetchall()
        D55C.phone.setText(str(v[0][2]))
        D55C.address.setText(v[0][3])
        D55C.username.setText(v[0][0])
        D55C.password.setText("*"*len(v[0][1]))
    D55C.newaddress.clear()
    D55C.newphone.clear()
    D55C.newusername.clear()
    D55C.newpass.clear()
    

def   back():
    D55C.close()
    D55.show()
    req = "SELECT doctor_username, doctor_password, doctor_name, speciality, phone,address FROM [Doctor log in] WHERE doctor_username = ? AND doctor_password = ?"
    cursor.execute(req, (username, password))
    v=cursor.fetchall()
    D55.hello.setText("Hello Doctor " + v[0][2] + " !")
    D55.doctor.setText(v[0][2])
    D55.speciality.setText(v[0][3])
    D55.phone.setText(str(v[0][4]))
    D55.address.setText(v[0][5])
    D55.username.setText(v[0][0])
    D55.password.setText("*"*len(v[0][1]))

def mail_sent():
    global username, password
    req = "SELECT  doctor_name FROM [Doctor log in] WHERE doctor_username = ? AND doctor_password = ?"
    cursor.execute(req, (username, password))
    v2=cursor.fetchall()
    mail =  D55.mail.toPlainText()
    subject = "Doctor " +v2[0][0] + ": " + D55.subject.text()
    if mail == "" or subject == "":
        mail_error("Complete the 2 fields: subject and mail text!")
    else:
        text = send_email(mail, "7689@holbertonstudents.com", subject)
        if text == "Email sent successfully!":
            D55.success.setText(text)
            D55.subject.clear()
            D55.mail.clear()
        else:
            mail_error(text)
            
        
    