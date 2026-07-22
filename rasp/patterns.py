# Attack Patterns

SQLI_PATTERNS = [
    "' OR 1=1",
    "' OR '1'='1",
    "UNION SELECT",
    "DROP TABLE",
    "SELECT *",
    "--",
    ";--",
    "information_schema"
]

XSS_PATTERNS = [
    "<script>",
    "</script>",
    "javascript:",
    "onerror=",
    "onload=",
    "<img",
    "<svg"
]

CMD_PATTERNS = [
    "&&",
    "||",
    ";",
    "|",
    "`",
    "$(",
    "bash",
    "sh "
]

TRAVERSAL_PATTERNS = [
    "../",
    "..\\",
    "/etc/passwd",
    "boot.ini",
    "win.ini"
]
