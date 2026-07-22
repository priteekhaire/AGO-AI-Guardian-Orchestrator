from patterns import *

def detect_attack(payload):

    payload = payload.lower()

    for pattern in SQLI_PATTERNS:
        if pattern.lower() in payload:
            return "SQL Injection"

    for pattern in XSS_PATTERNS:
        if pattern.lower() in payload:
            return "XSS"

    for pattern in CMD_PATTERNS:
        if pattern.lower() in payload:
            return "Command Injection"

    for pattern in TRAVERSAL_PATTERNS:
        if pattern.lower() in payload:
            return "Directory Traversal"

    return None
