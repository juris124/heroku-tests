import os
import csv
import math

# pieļaujamais min/max testa jomas simbolu nosaukuma garums
maxJoma=50
minJoma=5
# pieļaujamais min/max testa nosaukuma simbolu daudzums
maxTests=150
minTests=3
# pieļaujamais min/max testa jautājumu garuma simbolu daudzums
maxJautGarums=150
minJautGarums=3

def datnesStruktuurasParbaude(ielades_vieta,fails):
    
    with open(os.path.join(ielades_vieta, fails), newline='', encoding='utf-8') as csvfile:  
        lauki = ['jautajums', 'atbilde1', 'atbilde2', 'atbilde3', 'atbilde4']
        lasitajs = csv.DictReader(csvfile, fieldnames=lauki, delimiter=';')
        testa_joma = next(lasitajs)   
        if len(testa_joma["jautajums"]) < minJoma or len(testa_joma["jautajums"]) > maxJoma: 
            return (False,"Testa jomas nosaukums ir neatbilstošā garumā!")
       
        if testa_joma["jautajums"][0]!="#":
            return (False,"Testa faila pirmajai rindai jāsākas ar # !")    

        #print (testa_joma, testa_joma["atbilde1"])
        if testa_joma["atbilde1"] or testa_joma["atbilde2"] or testa_joma["atbilde3"] or testa_joma["atbilde4"]:            
            return (False,"Nepareiza faila struktūra! Faila 1. rindā jābūt tikai jomas nosaukumam!")
        
        testa_nosaukums = next(lasitajs)
        # paarbaudiit vai ir 4 atbildes, vai not NaN
        if len(testa_nosaukums["jautajums"]) < minTests or len(testa_nosaukums["jautajums"]) > maxTests: 
            return (False,"Testa nosaukums ir neatbilstošā garumā!")
        if testa_nosaukums["jautajums"][0]!="#":
            return (False,"Testa faila otrajai rindai jāsākas ar # !") 

        if testa_nosaukums["atbilde1"] or testa_nosaukums["atbilde2"] or testa_nosaukums["atbilde3"] or testa_nosaukums["atbilde4"]: 
            return (False,"Nepareiza faila struktūra! Faila 2. rindā jābūt tikai testa nosaukumam!")
        rindas_skaititajs=3
        for r in lasitajs:
            #print(rindas_skaititajs)
            if len(r["jautajums"]) < minJautGarums or len(r["jautajums"]) > maxJautGarums: 
                return (False,f"Jautājuma garums ir neatbilstošs! Problēma rindā nr. {rindas_skaititajs}, jautājums - {r['jautajums']}")
            
            if not r["atbilde1"] or not r["atbilde2"] or not r["atbilde3"] or not r["atbilde4"]: 
                return (False,f"Atbilžu versijām ir jābut tieši 4! Problēma rindā nr. {rindas_skaititajs}, jautājums - {r['jautajums']}")
            
            if len(r["atbilde1"]) == 0 or len(r["atbilde2"]) == 0 or len(r["atbilde3"]) == 0 or len(r["atbilde4"]) == 0: 
                return (False,f"Nekorektas atbilžu versijas Problēma rindā nr. {rindas_skaititajs}, jautājums - {r['jautajums']}")
            
            rindas_skaititajs+=1
            #pass
    return (True, "Viss ir OK, testa datne pārbaudīta un augšupielādēta testu mapē.")

def testuSaraksts(ielades_vieta):
    # te buus jaaveido list of list, lai padotu arii faila atrashanaas vietu prieksh dropdowna
    failuSaraksts = os.listdir(ielades_vieta)
    testuListe = []
    for datne in failuSaraksts:
        with open(os.path.join(ielades_vieta, datne), "r", encoding='utf-8') as f: 
            dati = f.readlines()
            testuListe.append([datne, dati[1].strip("#")])
    return testuListe 
