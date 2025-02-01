from cuid2 import cuid_wrapper
from typing import Callable

cuid: Callable[[], str] = cuid_wrapper()

MATCH_META_PATH = "match_meta.csv"

# for 関学2024
# types = [
#     ("男子本戦", 8),
#     ("男子コンソレーション", 6),
#     ("男子Aプレート", 5),
#     ("男子Bプレート", 4),
#     ("男子Cプレート", 3),
#     ("男子Dプレート", 2),
#     ("女子本戦", 7),
#     ("女子Aプレート", 5),
#     ("女子Bプレート", 4),
#     ("女子Cプレート", 3),
#     ("女子Dプレート", 2),
# ]

# for 関東新人2024
# (name, num_rounds, 決勝戦があるか)
# types = [
#     ("男子本戦", 7, True),
#     ("男子プレート", 2, False),
#     ("女子本戦", 6, True),
#     ("女子プレート", 1, False),
# ]

# for インカレ2024
# (name, num_rounds, 決勝戦があるか)
types = [
    ("選手権男子", 7, True),
    ("選手権女子", 6, True),
    ("選手権男子コンソレーション", 1, False),
    ("選手権女子コンソレーション", 1, False),
    ("新人男子", 6, True),
    ("新人女子", 6, True),
    ("新人男子コンソレーション", 1, False),
    ("新人女子コンソレーション", 1, False),
]

tournament_id = input("トーナメントIDを入力してください: ")

def next_line(f):
    f.write("\n")

with open(MATCH_META_PATH, "w") as f:
    f.write("id,type,tournament_id,is_rated,sex")

    for meta, num_rounds, has_final in types:
        sex = "男子" if "男子" in meta else "女子"
        if (has_final):
            if num_rounds > 2:
                for i in range(1, num_rounds - 2):
                    next_line(f)
                    f.write(f"{cuid()},{meta}{i}回戦,{tournament_id},True,{sex}")
                next_line(f)
                f.write(f"{cuid()},{meta}準々決勝,{tournament_id},True,{sex}")
            next_line(f)

            f.write(f"{cuid()},{meta}準決勝,{tournament_id},True,{sex}")
            next_line(f)
            f.write(f"{cuid()},{meta}3位決定戦,{tournament_id},True,{sex}")
            next_line(f)
            f.write(f"{cuid()},{meta}決勝,{tournament_id},True,{sex}")
        else:
            if num_rounds == 1:
                next_line(f)
                f.write(f"{cuid()},{meta},{tournament_id},True,{sex}")
            else:
                for i in range(1, num_rounds + 1):
                    next_line(f)
                    f.write(f"{cuid()},{meta}{i}回戦,{tournament_id},True,{sex}")
            # next_line(f)

