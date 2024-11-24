import re
from constant import TOKEN_PATTERNS

def compile_token_patterns(token_patterns):
    """
    Compile the token patterns into a list of regex objects.
    """
    return [(name, re.compile(pattern)) for name, pattern in token_patterns]

def tokenize(code):
    """
    Tokenizes the given code string using the provided token patterns.
    """
    compiled_patterns = compile_token_patterns(TOKEN_PATTERNS)  # Compile the token patterns
    tokens = []  # List to store the tokens
    position = 0  # Current position in the code string
    line_number = 1  # Track line numbers

    while position < len(code):
        match_found = False  # Flag to check if a match is found

        for token_name, token_regex in compiled_patterns:
            # Try to match the pattern at the current position
            match = token_regex.match(code, position)
            if match:
                match_found = True
                value = match.group(0)  # Get the matched value
                position = match.end()  # Update the position

                # Count newlines for line tracking
                line_number += value.count('\n')

                # Ignore comments and whitespace
                if token_name not in ("COMMENT", "WHITESPACE"):
                    tokens.append((value, token_name, line_number))  # Add the token to the list
                break

        if not match_found:
            # Raise an error if no match is found
            raise ValueError(f"Unexpected character at position {position}: {code[position]}")

    return tokens  # Return the list of tokens

def display_tokens(tokens):
    """
    Displays the tokens in a tabular format with lexeme, token type, and line number.
    """
    # Print the table header
    print(f"{'Lexemes':<15} {'Tokens':<15} {'Line':<5}")
    print(f"{'-' * 15} {'-' * 15} {'-' * 5}")

    # Print each token in the table
    for lexeme, token_type, line in tokens:
        print(f"{lexeme:<15} {token_type:<15} {line:<5}")
