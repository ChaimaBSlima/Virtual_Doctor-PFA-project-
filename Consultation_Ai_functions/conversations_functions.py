from PyQt5.QtWidgets import QApplication
import speech_recognition as sr
import pyttsx3
from windows_functions.loading_windows import D2D, D2Z
from Consultation_Ai_functions.speech_recognition_functions import*
from Consultation_Ai_functions.compute_similarity_function import*
from Consultation_Ai_functions.start_questions_functions import *
from Consultation_Ai_functions.shared_variables import *
from Health_Data.data_relation import*
####SET SPEECH####
recognizer = sr.Recognizer()
engine = pyttsx3.init()
Male = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
Female = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'



####SET DATA###

query = """
SELECT symptoms_id, symptoms_answers, [Diseases ID]
FROM symptoms
WHERE [Diseases ID] <> 11
ORDER BY symptoms_id
"""
query1 = """
SELECT symptoms_id, symptoms_answers, [Diseases ID]
FROM symptoms
WHERE [Diseases ID] = 11
ORDER BY symptoms_id
"""
def conversation_with_zira():
    global query, diseases, D2Z, query1
    test = False
    while True:       
        if test == True:
            break
        engine.setProperty('voice', Female)
        respondZ("Hello, how are you doing today?")
        input_text = recognize_speechZ()

        if input_text != "Sorry, I couldn't understand what you said." and input_text != "Could not request results" and input_text != "" and not test:
            D2Z.listen.setText("Analyzing your speech .. Please wait! ..")
            QApplication.processEvents()
            cursor.execute(query)
            results = cursor.fetchall()
            diseases_doupt = 1
            
            for i in range(len(results)):
                text2 = results[i][1]
                if compute_similarity(text2, input_text) > 60:
                    if results[i][2] not in diseases[:diseases_doupt]:
                        test = True
                        diseases[diseases_doupt] = results[i][2]
                        diseases_doupt += 1
            
            if test:
                break  
        else:
            respondZ("Sorry, I couldn't understand what you said.")
            respondZ("Please provide valuable information about your health situation!")
            continue  

        if not test:
            cursor.execute(query1)
            results1 = cursor.fetchall()
            
            for i in range(len(results1)):
                text2 = results1[i][1]
                if compute_similarity(text2, input_text) > 60:
                    test = True
                    break  
            
            if not test:
                respondZ("Please provide valuable information about your health situation!")
                continue  

    start_questionsZ(diseases_doupt)

def conversation_with_david():
    global query, diseases, D2D, query1
    test = False
    while True:
        if test == True:
            break
        engine.setProperty('voice', Male)
        respondD("Hello, how are you doing today?")
        input_text = recognize_speechD()

        if input_text != "Sorry, I couldn't understand what you said." and input_text != "Could not request results" and input_text != "" and not test:
            D2D.listen.setText("Analyzing your speech .. Please wait! ..")
            QApplication.processEvents()
            cursor.execute(query)
            results = cursor.fetchall()
            diseases_doupt = 1
            
            for i in range(len(results)):
                text2 = results[i][1]
                if compute_similarity(text2, input_text) > 60:
                    if results[i][2] not in diseases[:diseases_doupt]:
                        test = True
                        diseases[diseases_doupt] = results[i][2]
                        diseases_doupt += 1
            
            if test:
                break  
        else:
            respondD("Sorry, I couldn't understand what you said.")
            respondD("Please provide valuable information about your health situation!")
            continue  

        if not test:
            cursor.execute(query1)
            results1 = cursor.fetchall()
            
            for i in range(len(results1)):
                text2 = results1[i][1]                
                if compute_similarity(text2, input_text) > 60:
                    test = True
                    break  
            
            if not test:
                respondD("Please provide valuable information about your health situation!")
                continue  

    start_questionsD(diseases_doupt)