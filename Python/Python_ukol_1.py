from collections import Counter

with open("alice.txt", encoding = "utf-8") as file:           
    text = file.read()                         # uloží se řetězec
    text = text.lower()                        # převod na malá písmena
    text = text.replace(" ","")                # odstranění mezer
    text = text.replace("\n","")               # odstranění zalomení
#print(text)

seznam_znaku = list(text)                      # převede řetězec na seznam písmen
#print(seznam_pismen)

cetnost_znaku = Counter(seznam_znaku)          # vytvoří slovník, kde klíče jsou znaky a hodnoty počet znaků
sort_keys = sorted(cetnost_znaku.keys())       # seznam klíčů sežazených podle abecedy

slovnik_znaku ={}                              # do slovnik_znaku vkládám hodnoty podle abecedy
for i in sort_keys:    
    for j in cetnost_znaku.keys():
       if j == i:
          slovnik_znaku[i] = cetnost_znaku[j]    # výpis hodnot pro jednotlivá písmena podle abecedy, jen čísla (cetnost_znaku["a"] = 8826)

for key, value in slovnik_znaku.items():
    print(f"{key} : {value} \n")

import json
with open('ukol1_output.json', 'w', encoding='utf-8') as out:          # zapíše do souboru
    json.dump(slovnik_znaku, out, ensure_ascii = False, indent = 2)

