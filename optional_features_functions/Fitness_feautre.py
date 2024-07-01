from math import*

def fitness(age, taille, poids, mince, moyen, large):
    IMC=round((poids)/((taille/100)**2),2)
    if mince==True:
         PI=round(((taille-100) +(age/10))*0.9*0.9,2)
    elif moyen==True:
        PI=round(((taille-100) +(age/10))*0.9,2)
    else:
        PI=round(((taille-100) +(age/10))*0.9*1.1,2)
    return(IMC, PI)