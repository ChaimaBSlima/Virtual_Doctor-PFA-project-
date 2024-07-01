from Consultation_Ai_functions.speech_recognition_functions import*
from Consultation_Ai_functions.compute_similarity_function import*
from Consultation_Ai_functions.shared_variables import *
from Consultation_Ai_functions.Ai_analyzing_results_functions import *
from Health_Data.data_relation import*

def start_questionsZ(n):
    global diseases
    points = 0
    for j in range(n):
        BigReq = "select number_symptomps from Diseases where Diseases.[Diseases ID] ="+str(diseases[j])
        cursor.execute(BigReq)
        T= cursor.fetchall()
        i = 0
        while i < T[0][0]:  
            req="select symptoms_questions,symptoms_points from Diseases,symptoms where Diseases.[Diseases ID] = symptoms.[Diseases ID]  and Diseases.[Diseases ID]="+str(diseases[j])+ " and symptoms.line="+str(i)
            cursor.execute(req)
            v=cursor.fetchall()
            respondZ(v[0][0])
            input_text = recognize_speechZ()
            if compute_similarity(input_text,"Yes")>50:
                points+=v[0][1]
                print(points)
                i+=1
            elif compute_similarity(input_text,"No")>45:
                points+= 0
                print(points)
                i+=1
            else:
                if input_text == "Could not request results" or input_text == "Sorry, I couldn't understand what you said.":
                    respondZ(input_text)
                respondZ("Can you please answer with yes or No?")
    Ai_analyzing_resultZ(n,points)

def start_questionsD(n):
    global diseases
    points = 0
    for j in range(n):
        BigReq = "select number_symptomps from Diseases where Diseases.[Diseases ID] ="+str(diseases[j])
        cursor.execute(BigReq)
        T= cursor.fetchall()
        i = 0
        while i < T[0][0]:  
            req="select symptoms_questions,symptoms_points from Diseases,symptoms where Diseases.[Diseases ID] = symptoms.[Diseases ID]  and Diseases.[Diseases ID]="+str(diseases[j])+ " and symptoms.line="+str(i)
            cursor.execute(req)
            v=cursor.fetchall()
            respondD(v[0][0])
            input_text = recognize_speechD()
            if compute_similarity(input_text,"Yes")>50:
                points+=v[0][1]
                print(points)
                i+=1
            elif compute_similarity(input_text,"No")>45:
                points+= 0
                print(points)
                i+=1
            else:
                if input_text == "Could not request results" or input_text == "Sorry, I couldn't understand what you said.":
                    respondD(input_text)
                respondD("Can you please answer with yes or No?")
    Ai_analyzing_resultD(n,points)