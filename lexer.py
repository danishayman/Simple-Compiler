import re
from constant import TOKEN_PATTERNS

def tokenize(source_code):
    tokens = []
    pos = 0
    line = 1
    
    while pos < len(source_code):
        match = None
        for token_type, pattern in TOKEN_PATTERNS:
            regex = re.compile(pattern)
            match = regex.match(source_code, pos)
            if match:
                lexeme = match.group(0)
                if token_type != 'WHITESPACE' and token_type != 'COMMENT':  # Ignore whitespace and comments
                    tokens.append((lexeme, token_type))
                pos = match.end(0)
                line += lexeme.count('\n')  # Increment line count for newlines
                break

        if not match:
            # Handle unrecognized characters
            raise ValueError(f"Lexical error at line {line}: '{source_code[pos]}'")

    return tokens

def print_tokens(tokens):
    # Header
    print(f"{'Lexemes':<10} {'Tokens'}")
    print(f"{'-------':<10} {'------'}")
    # Print each token on a new line
    for lexeme, token_type in tokens:
        print(f"{lexeme:<10} {token_type}")