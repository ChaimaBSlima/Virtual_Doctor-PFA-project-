from Health_Data.data_relation import*

def calculate_foodHealth(item,ligne,typefood):
    #req="select food.*,typefood.* from food, typefood where food.id-type=typefood.id-type"
    req="select Lipids,Carbohydrates,Proteins from typefood,food where typefood.id_type = food.id_type and typefood.libelle='"+typefood+"' and food.ligne="+str(ligne)
    cursor.execute(req)
    v=cursor.fetchall()
    lip= (int(item)*(v[0][0]))/100
    glu= (int(item)*(v[0][1]))/100
    prot= (int(item)*(v[0][2]))/100
    return(lip, glu, prot)
def Bilan_calculation(lip, glu, prot):
    lip=lip*9
    glu=glu*4
    prot=prot*4
    Bilan=lip+glu+prot
    lip=(lip*100)/Bilan
    glu=(glu*100)/Bilan
    prot=(prot*100)/Bilan
    return(lip, glu, prot)