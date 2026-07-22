# MITRE ATT&CK Mapper

MITRE_MAPPING = {
    "SQL Injection": {
        "mitre_id": "T1190",
        "technique": "Exploit Public-Facing Application",
        "tactic": "Initial Access"
    },

    "XSS": {
        "mitre_id": "T1190",
        "technique": "Exploit Public-Facing Application",
        "tactic": "Initial Access"
    },

    "Command Injection": {
        "mitre_id": "T1059",
        "technique": "Command and Scripting Interpreter",
        "tactic": "Execution"
    },

    "Brute Force": {
        "mitre_id": "T1110",
        "technique": "Brute Force",
        "tactic": "Credential Access"
    },

    "Directory Traversal": {
        "mitre_id": "T1190",
        "technique": "Exploit Public-Facing Application",
        "tactic": "Initial Access"
    },

    "Unknown": {
        "mitre_id": "N/A",
        "technique": "Unknown",
        "tactic": "Unknown"
    }
}


def map_attack(attack):
    return MITRE_MAPPING.get(
        attack,
        MITRE_MAPPING["Unknown"]
    )
