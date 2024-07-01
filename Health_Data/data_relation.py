import pyodbc
cnn_string = (r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Chaima Ben slima\Virtual_Doctor-PFA-project-\Health_Data\Data.mdb;')
try:
    global cursor
    cnn = pyodbc.connect(cnn_string)
    print("connection successful")
    cursor = cnn.cursor()    
except pyodbc.Error as e:
    print(e)