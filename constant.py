TOKEN_PATTERNS = [
    # Keywords
    ("KEYWORD", r'\b(if|else|print|while|for|int|return)\b'),

    # Identifiers
    ("IDENTIFIER", r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),

    # Literals
    ("INTEGER", r'\b\d+\b'),
    ("FLOAT", r'\b\d+\.\d+\b'),
    ("STRING", r'"[^"]*"'),  # Basic string support
    ("BOOLEAN", r'\b(true|false)\b'),

    # Operators
    ("ASSIGNMENT", r'='),
    ("ARITHMETIC", r'[+\-*/]'),
    ("COMPARISON", r'(>=|<=|==|!=|[><=])'),

    # Punctuation
    ("LBRACE", r'\{'),
    ("RBRACE", r'\}'),
    ("LPAREN", r'\('),
    ("RPAREN", r'\)'),
    ("SEMICOLON", r';'),

    # Comments
    ("COMMENT", r'//.*'),

    # Whitespace (ignored)
    ("WHITESPACE", r'\s+'),
]