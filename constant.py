# Description: This file contains the constant values used in the compiler.
TOKEN_PATTERNS = [
    # Keywords
    ("KEYWORD", r'\b(if|else|print|while|for|int|float|return|def)\b'),

    # Identifiers
    ("IDENTIFIER", r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),

    # Literals
    ("INTEGER", r'\b\d+\b'),
    ("FLOAT", r'\b\d+\.\d+\b'),
    ("STRING", r'"[^"]*"'),  
    ("BOOLEAN", r'\b(true|false)\b'),

    # Operators
    ("ASSIGNMENT", r'='),
    ("ARITHMETIC", r'[+\-*/%]'),  
    ("COMPARISON", r'(>=|<=|!=|[><])'),
    ("EQUALITY", r'=='),

    # Punctuation
    ("LBRACE", r'\{'),
    ("RBRACE", r'\}'),
    ("LPAREN", r'\('),
    ("RPAREN", r'\)'),
    ("SEMICOLON", r';'),
    ("COMMA", r','),

    # Comments (ignored)
    ("COMMENT", r'//.*'),

    # Whitespace (ignored)
    ("WHITESPACE", r'\s+'),
]