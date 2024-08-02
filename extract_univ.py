import pandas as pd

male = pd.read_excel('players.xlsx', sheet_name="Sheet1", index_col=0)
female = pd.read_excel('players.xlsx', sheet_name="Sheet2", index_col=0)

df = pd.concat([male, female], axis=0)

universities_set = set({})

for i, row in df.iterrows():
    universities_set.add(row['大学名'])

def next_line(f):
    f.write('\n')

UNIV_FILE = 'universities.json'

with open(UNIV_FILE, 'w') as f:
    f.write('[')
    next_line(f)

    for i, univ_name in enumerate(universities_set):
        f.write('  {')
        next_line(f)
        f.write('    "id": ' + str(i+1) + ',')
        next_line(f)
        f.write('    "name": "' + univ_name + '",')
        next_line(f)
        f.write('    "shortName": "",')
        next_line(f)
        f.write('    "region": "関東"')
        next_line(f)
        f.write('  }')
        if i != len(universities_set) - 1:
            f.write(',')
        next_line(f)

    f.write(']')
