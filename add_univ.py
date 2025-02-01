
import pandas as pd
import json

male = pd.read_excel('players.xlsx', sheet_name="Sheet1", index_col=0)
female = pd.read_excel('players.xlsx', sheet_name="Sheet2", index_col=0)

df = pd.concat([male, female], axis=0)

universities_set = set({})

for i, row in df.iterrows():
    universities_set.add(row['大学名'])

UNIV_FILE = 'universities.json'
ORIGIN_FILE = 'universities_origin.json'

with open(UNIV_FILE, 'w') as f:
    with open(ORIGIN_FILE, 'r') as f_origin:
        new_univ_list = json.load(f_origin)
        old_univ_names = list(map(lambda x: x['name'], new_univ_list))
        last_id = len(new_univ_list)

        for univ_name in universities_set:
            if univ_name not in old_univ_names:
                last_id += 1
                new_univ = {
                    "id": last_id,
                    "name": univ_name,
                    "shortName": "",
                    "region": ""
                }
                new_univ_list.append(new_univ)

        json.dump(new_univ_list, f, ensure_ascii=False, indent=4)
