from nq.sb import bjrun

map_input = """26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna"""

virus_input = """7
6
1 2
2 3
1 5
5 2
5 6
4 7"""

tree_input = """50
30
24
5
28
45
98
52
60"""

heap_input = """13
0
1
2
0
0
3
2
1
0
0
0
0
0"""

heap_input_2 = """100
1
2
3
4
5
6
7
8
9
10
1
2
3
4
5
6
7
8
9
10
1
2
3
4
5
6
7
8
9
10
1
2
3
4
5
6
7
8
9
10
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
2
3
4
5
6
7
8
9
10
0
0
0
0
0
0
0
0
0
0"""

tests = [
    ("00_poke_master.py", map_input),
    ("01_virus.py", virus_input),
    ("02_tree.py", tree_input),
    ("03_heap.py", heap_input),
    ("03_heap.py", heap_input_2),
]

for fp, input_text in tests:
    bjrun(fp, input_text)
