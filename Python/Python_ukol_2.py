lines = []    # seznam řádků

with open('netflix_titles.tsv', encoding='utf-8') as file:
    for line in file:
        lines.append(line)                  # co řádek, to prvek seznamu. Řádky jsou oddělené \n. 505 řádků

tabulka = []
null = []
for radky in lines[1:]:                      # první řádek vynechá
    slova = radky.split("\t")                # řádek rozdělí do prvků seznamu, rozdělovač je \t  Aby se to uložilo do seznamu, musím to uložit do proměnné slova! Jinak to zůstane string.
    if slova[16] == '':                      # Kontrola, zda je pole 'cast nebo 'directors' prázdné a přiřazení hodnoty 'null'
        cast = null
    else: cast = slova[16].split(",")        # cast do seznamu  
    for i in range(len(cast)):               # odstranění mezer před jmény
        cast[i] = cast[i].strip()
    if slova[15] == '':                     
        directors = null
    else: directors = slova[15].split(",")   # directors do seznamu
    decade = str(slova[19])[:3] + "0"        # odebrání poslední číslice a přidání nuly
    seznam = {"title" : slova[2],            # Vytvoření slovníku pro aktuální řádek
              "directors" : directors, 
              "cast" : cast, 
              "genres" : slova[8], 
              "decade" : decade} 
    tabulka.append(seznam)                   # přidání slovníku do seznamu

for i in tabulka :                           # tisk tabulky po řádcích
    print(i)

import json
with open('movies.json', 'w', encoding='utf-8') as output_file:  # uložení do souboru movies.json
    json.dump(tabulka, output_file, indent = 4 )

