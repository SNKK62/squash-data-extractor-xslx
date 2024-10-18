from cuid2 import cuid_wrapper
from typing import Callable

cuid: Callable[[], str] = cuid_wrapper()

MATCH_META_PATH = "match_meta.csv"

# for インカレ予選2024
# (name, num_rounds, 決勝戦があるか, ３決があるか)
types = [
    ("選手権男子", 4),
    ("選手権女子", 3),
    ("新人男子", 3),
    ("新人女子", 2),
]

tournament_id = input("トーナメントIDを入力してください: ")

def next_line(f):
    f.write("\n")

with open(MATCH_META_PATH, "w") as f:
    f.write("id,type,tournament_id,is_rated,sex")

    for meta, num_rounds in types:
        for i in range(1, num_rounds):
            next_line(f)
            f.write(f"{cuid()},{meta}{i}回戦,{tournament_id},True,{'男子' if '男子' in meta else '女子'}")
        next_line(f)
        f.write(f"{cuid()},{meta}インカレ決定戦,{tournament_id},True,{'男子' if '男子' in meta else '女子'}")

