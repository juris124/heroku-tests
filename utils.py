import os
import csv

def datnesStruktuurasParbaude(ielades_vieta,fails):
    
    with open(os.path.join(ielades_vieta, fails), newline='', encoding='utf-8') as csvfile:  
        lauki = ['jautajums', 'atbilde1', 'atbilde2', 'atbilde3', 'atbilde4']
        lasitajs = csv.DictReader(csvfile, fieldnames=lauki, delimiter=';')
        testa_joma = next(lasitajs)   
        if len(testa_joma["jautajums"]) < 5 or len(testa_joma["jautajums"]) > 50: 
            return (False,"Testa jomas nosaukums ir neatbilstošā garumā!")
        #print (testa_joma, testa_joma["atbilde1"])
        if testa_joma["atbilde1"] or testa_joma["atbilde2"] or testa_joma["atbilde3"] or testa_joma["atbilde4"]:            
            return (False,"Nepareiza faila struktūra! Faila 1. rindā jābūt tikai jomas nosaukumam!")
        
        testa_nosaukums = next(lasitajs)
        if len(testa_nosaukums["jautajums"]) < 3 or len(testa_nosaukums["jautajums"]) > 150: 
            return (False,"Testa nosaukums ir neatbilstošā garumā!")
        if testa_nosaukums["atbilde1"] or testa_nosaukums["atbilde2"] or testa_nosaukums["atbilde3"]or testa_nosaukums["atbilde4"]: 
            return (False,"Nepareiza faila struktūra! Faila 2. rindā jābūt tikai testa nosaukumam!")
        rindas_skaititajs=3
        for r in lasitajs:
            #print(rindas_skaititajs)
            if len(r["jautajums"]) < 3 or len(r["jautajums"]) > 100: 
                return (False,f"Jautājuma garums ir neatbilstošs! Problēma rindā nr. {rindas_skaititajs}, jautājums - {r['jautajums']}")
            if len(r["atbilde1"]) == 0 or len(r["atbilde2"]) == 0 or len(r["atbilde3"]) == 0 or len(r["atbilde4"]) == 0: 
                return (False,f"Nekorektas atbilžu versijas Problēma rindā nr. {rindas_skaititajs}, jautājums - {r['jautajums']}")
            rindas_skaititajs+=1
            #pass
    return (True, "Viss ir OK, testa datne pārbaudīta un augšupielādēta testu mapē.")