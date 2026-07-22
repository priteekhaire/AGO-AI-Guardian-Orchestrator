from mitre_mapper import map_attack

attacks = [
    "SQL Injection",
    "XSS",
    "Command Injection",
    "Brute Force",
    "Directory Traversal",
    "Random Attack"
]

for attack in attacks:

    result = map_attack(attack)

    print("=" * 60)
    print(f"Attack     : {attack}")
    print(f"MITRE ID   : {result['mitre_id']}")
    print(f"Technique  : {result['technique']}")
    print(f"Tactic     : {result['tactic']}")
