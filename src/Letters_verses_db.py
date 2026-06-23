from ast import literal_eval
import json
import pandas as pd
df = pd.read_csv("arabic_poems.csv")
letters_db = {}

for index, row in df.iterrows():
    for verse in literal_eval(row['verses']):
        first_letter = verse[0]
        if first_letter not in letters_db:
            letters_db[first_letter] = []
        letters_db[first_letter].append({
           "category":row['category'],
           "verse":verse
        })


with open("verses_database.json", "w", encoding="utf-8") as f:
    json.dump(letters_db, f, ensure_ascii= False, indent=4)