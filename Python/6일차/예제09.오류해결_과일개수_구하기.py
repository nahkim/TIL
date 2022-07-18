from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:

    if fruit not in fruit_count:
        # fruit_count = {fruit: 1}
        # 이렇게 쓸 경우 여기에 들어올때마다 fruit_count에 있는 값이 다 사라지고 {fruit : 1}만 계속해서 남게됨
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)