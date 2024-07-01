from PyQt5.QtCore import QTimer
from windows_functions.bubble_speech_functions import  bubble1
from windows_functions.shared_variables import index1, timer1
from windows_functions.loading_windows import  D1


def mainwindow():
    global index1, timer1
    D1.show()
    D1.l1.setText("Hello! I am your")
    D1.l2.setText("virtual doctor")
    timer1 = QTimer()
    timer1.timeout.connect(bubble1)
    timer1.start(5000)