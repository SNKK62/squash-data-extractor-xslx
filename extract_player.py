import pandas as pd

male = pd.read_excel('players.xlsx', sheet_name="Sheet1", index_col=0)
female = pd.read_excel('players.xlsx', sheet_name="Sheet2", index_col=0)

def next_line(f):
    f.write('\n')

UNIV_FILE = 'universities.json'

def is_str(s):
    return s.startswith('"') and s.endswith('"')

def remove_quote(s):
    return s[1:-1]

univ_data = {}

with open(UNIV_FILE) as uf:
    while True:
        name = ''
        line = uf.readline().strip()
        if line == '[':
            continue
        elif line == ']':
            break
        elif line == '{':
            univ = {}
            while True:
                line = uf.readline().strip()
                if line.startswith('}'):
                    break
                if line.endswith(','):
                    line = line[:-1]
                key, value = line.split(':')
                key = remove_quote(key.strip())
                value = value.strip()

                if is_str(value):
                    value = remove_quote(value)
                    univ[key] = value
                    if key == "name":
                        name = value
                else:
                    univ[key] = int(value)

            univ_data[name] = univ

print(univ_data)

PLAYER_FILE = 'players.json'
with open(PLAYER_FILE, 'w') as f:
    f.write('[')
    next_line(f)

    for i, row in male.iterrows():
        f.write('  {')
        next_line(f)
        f.write('    "firstName": "' + row["選手名"].split(" ")[1] + '",')
        next_line(f)
        f.write('    "lastName": "' + row["選手名"].split(" ")[0] + '",')
        next_line(f)
        f.write('    "grade": ' + str(row["年次"]) + ',')
        next_line(f)
        f.write('    "universityId": ' + str(univ_data[row["大学名"]]["id"]) + ',')
        next_line(f)
        f.write('    "sex": "男子",')
        next_line(f)
        f.write('    "isRetired": false')
        next_line(f)
        f.write('  }')
        f.write(',')
        next_line(f)

    for i, row in female.iterrows():
        f.write('  {')
        next_line(f)
        f.write('    "firstName": "' + row["選手名"].split(" ")[1] + '",')
        next_line(f)
        f.write('    "lastName": "' + row["選手名"].split(" ")[0] + '",')
        next_line(f)
        f.write('    "grade": ' + str(row["年次"]) + ',')
        next_line(f)
        f.write('    "universityId": ' + str(univ_data[row["大学名"]]["id"]) + ',')
        next_line(f)
        f.write('    "sex": "女子",')
        next_line(f)
        f.write('    "isRetired": false')
        next_line(f)
        f.write('  }')
        if i != len(female):
            f.write(',')
        next_line(f)

    f.write(']')
