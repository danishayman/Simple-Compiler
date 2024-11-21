import re

# Define token patterns
TOKEN_PATTERNS = [
    ("KEYWORD", r'\b(if|else|print|while|for|int|float|return|def)\b'),
    ("IDENTIFIER", r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ("INTEGER", r'\b\d+\b'),
    ("FLOAT", r'\b\d+\.\d+\b'),
    ("STRING", r'"[^"]*"'),
    ("BOOLEAN", r'\b(true|false)\b'),
    ("ASSIGNMENT", r'='),
    ("ARITHMETIC", r'[+\-*/%]'),
    ("COMPARISON", r'(>=|<=|!=|[><])'),
    ("EQUALITY", r'=='),
    ("LBRACE", r'\{'),
    ("RBRACE", r'\}'),
    ("LPAREN", r'\('),
    ("RPAREN", r'\)'),
    ("SEMICOLON", r';'),
    ("COMMA", r','),
    ("COMMENT", r'//.*'),
    ("WHITESPACE", r'\s+'),
]

def compile_token_patterns(token_patterns):
    """
    Compile the token patterns into a list of regex objects.
    """
    return [(name, re.compile(pattern)) for name, pattern in token_patterns]

def tokenize(code):
    """
    Tokenizes the given code string using the provided token patterns.
    """
    compiled_patterns = compile_token_patterns(TOKEN_PATTERNS)
    tokens = []
    position = 0
    line_number = 1  # Track line numbers

    while position < len(code):
        match_found = False

        for token_name, token_regex in compiled_patterns:
            # Try to match the pattern at the current position
            match = token_regex.match(code, position)
            if match:
                match_found = True
                value = match.group(0)
                position = match.end()

                # Count newlines for line tracking
                line_number += value.count('\n')

                # Ignore comments and whitespace
                if token_name not in ("COMMENT", "WHITESPACE"):
                    tokens.append((value, token_name, line_number))
                break

        if not match_found:
            raise ValueError(f"Unexpected character at position {position}: {code[position]}")

    return tokens

def display_tokens(tokens):
    """
    Displays the tokens in a tabular format with lexeme, token type, and line number.
    """
    print(f"{'Lexemes':<15} {'Tokens':<15} {'Line':<5}")
    print(f"{'-' * 15} {'-' * 15} {'-' * 5}")

    for lexeme, token_type, line in tokens:
        print(f"{lexeme:<15} {token_type:<15} {line:<5}")
