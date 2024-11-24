# Description: This file contains the constant values used in the compiler.

TOKEN_PATTERNS = [
    # Keywords: match reserved words in the language
    ("KEYWORD", r'\b(if|else|print|while|for|int|float|return|def)\b'),

    # Identifiers: match variable/function names
    ("IDENTIFIER", r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),

    # Literals: match integer, float, string, and boolean values
    ("INTEGER", r'\b\d+\b'),
    ("FLOAT", r'\b\d+\.\d+\b'),
    ("STRING", r'"[^"]*"'),  
    ("BOOLEAN", r'\b(true|false)\b'),

    # Operators: match assignment, arithmetic, and comparison operators
    ("ASSIGNMENT", r'='),
    ("ARITHMETIC", r'[+\-*/%]'),  
    ("COMPARISON", r'(>=|<=|!=|[><])'),
    ("EQUALITY", r'=='),

    # Punctuation: match braces, parentheses, semicolons, and commas
    ("LBRACE", r'\{'),
    ("RBRACE", r'\}'),
    ("LPAREN", r'\('),
    ("RPAREN", r'\)'),
    ("SEMICOLON", r';'),
    ("COMMA", r','),

    # Comments: match single-line comments (ignored)
    ("COMMENT", r'//.*'),

    # Whitespace: match spaces, tabs, and newlines (ignored)
    ("WHITESPACE", r'\s+'),
]