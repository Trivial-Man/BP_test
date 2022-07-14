"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Parakary-less Boo's Portrait.
"""
edges_obk_add_boo_portrait_kooper = [
    {"from": {"map": "OBK_06", "id": 0}, "to": {"map": "OBK_06", "id": "ItemA"},  "reqs": [["Kooper"]], "mapchange": False}, #* Library Fall From Ceiling -> ItemA (BooPortrait)
    {"from": {"map": "OBK_06", "id": "ItemA"},  "to": {"map": "OBK_06", "id": 0}, "reqs": [], "mapchange": False}, #* ItemA (BooPortrait) -> Library Fall From Ceiling
]

edges_obk_add_boo_portrait_laki = [
    {"from": {"map": "OBK_06", "id": 1}, "to": {"map": "OBK_06", "id": "ItemA"}, "reqs": [["Lakilester"]], "mapchange": False}, #* Library Bombable Wall -> ItemA (BooPortrait)
    {"from": {"map": "OBK_06", "id": "ItemA"},  "to": {"map": "OBK_06", "id": 0}, "reqs": [["Lakilester"]], "mapchange": False}, #* ItemA (BooPortrait) -> Library Fall From Ceiling
    {"from": {"map": "OBK_06", "id": 1}, "to": {"map": "OBK_06", "id": 0}, "reqs": [["Lakilester"]], "mapchange": False}, #* Library Bombable Wall -> Library Fall From Ceiling
    {"from": {"map": "OBK_06", "id": 0}, "to": {"map": "OBK_05", "id": 1},  "reqs": [["Lakilester"]], "mapchange": False}, # Library Fall From Ceiling -> Pot Room Hole Under Planks
]