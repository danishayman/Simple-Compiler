class Parser:
    def __init__(self, tokens):
        self.tokens = tokens  # List of tokens to parse
        self.current_index = 0  # Index of the current token
        self.current_token = self.tokens[self.current_index]  # The current token being parsed
        self.parse()  # Start parsing

    def parse(self):
        """
        Parse the whole program.
        """
        print("Parsing program...")
        self.program()

    def program(self):
        """
        Parse the program, which is a sequence of statements.
        """
        while not self.is_at_end():
            self.statement()

    def statement(self):
        """
        Parse a statement (assignment, if, print, etc.).
        """
        if self.match("IDENTIFIER"):
            self.assignment_statement()
        elif self.match("KEYWORD", "if"):
            self.if_statement()
        elif self.match("KEYWORD", "print"):
            self.print_statement()
        else:
            self.error("Unexpected statement.")

    def assignment_statement(self):
        """
        Parse an assignment statement (e.g., x = 5;).
        """
        self.consume("IDENTIFIER")  # Variable name
        self.consume("ASSIGNMENT")  # '='
        self.expression()  # Expression on the right-hand side
        self.consume("SEMICOLON")  # ';'
        print("Parsed assignment statement.")
        print("\n")

    def if_statement(self):
        """
        Parses an if statement, including else if and else blocks.
        """
        self.consume("KEYWORD", "if")
        self.consume("LPAREN")  # Expect '('
        self.expression()  # Parse the condition inside parentheses

        if not self.match("RPAREN"):  # Check if closing parenthesis is missing
            self.error("Missing closing parenthesis for if condition.")
        self.consume("RPAREN")  # Consume ')'

        print("Parsed if condition.")
        print("\n")

        self.consume("LBRACE")  # Expect '{'
        while self.current_token and self.current_token[1] != "RBRACE":
            self.statement()
        if not self.match("RBRACE"):  # Check if closing brace is missing
            self.error("Missing closing brace for if block.")
        self.consume("RBRACE")  # Consume '}'

        print("Parsed if block.")
        print("\n")

        # Handle else-if and else blocks similarly, ensuring proper matching
        while self.match("KEYWORD", "else") and self.check_next("KEYWORD", "if"):
            self.consume("KEYWORD", "else")
            self.consume("KEYWORD", "if")
            self.consume("LPAREN")
            self.expression()
            if not self.match("RPAREN"):
                self.error("Missing closing parenthesis for else-if condition.")
            self.consume("RPAREN")
            print("Parsed else-if condition.")
            print("\n")

            self.consume("LBRACE")
            while self.current_token and self.current_token[1] != "RBRACE":
                self.statement()
            if not self.match("RBRACE"):
                self.error("Missing closing brace for else-if block.")
            self.consume("RBRACE")
            print("Parsed else-if block.")
            print("\n")

        if self.match("KEYWORD", "else"):
            self.consume("KEYWORD", "else")
            self.consume("LBRACE")
            while self.current_token and self.current_token[1] != "RBRACE":
                self.statement()
            if not self.match("RBRACE"):
                self.error("Missing closing brace for else block.")
            self.consume("RBRACE")
            print("Parsed else block.")
            print("\n")

    def check_next(self, expected_type, expected_lexeme=None):
        """
        Checks the next token without consuming it.
        """
        if self.current_index + 1 < len(self.tokens):
            next_token = self.tokens[self.current_index + 1]
            return next_token[1] == expected_type and (expected_lexeme is None or next_token[0] == expected_lexeme)
        return False

    def print_statement(self):
        """
        Parse a print statement (e.g., print(x);).
        """
        self.consume("KEYWORD", "print")
        self.consume("LPAREN")  # '('
        self.expression()  # Expression inside print
        self.consume("RPAREN")  # ')'
        self.consume("SEMICOLON")  # ';'
        print("Parsed print statement.")
        print("\n")

    def statement_list(self):
        """
        Parse a list of statements inside a block.
        """
        while not self.match("RBRACE") and not self.is_at_end():
            self.statement()

    def expression(self):
        """
        Parses an expression, which may consist of terms connected by 
        arithmetic operators or comparison operators.
        """
        self.term()  # Parse the first term

        # Check for ARITHMETIC or COMPARISON operator
        while self.current_token and self.current_token[1] in ("ARITHMETIC", "COMPARISON"):
            operator_type = self.current_token[1]
            self.consume(operator_type)  # Consume the operator
            self.term()  # Parse the next term

    def term(self):
        """
        Parses a term, which could be a single identifier, integer, or expression in parentheses.
        """
        if self.current_token[1] == "INTEGER" or self.current_token[1] == "IDENTIFIER":
            self.consume(self.current_token[1])  # Consume INTEGER or IDENTIFIER token type
        elif self.current_token[1] == "LPAREN":
            self.consume("LPAREN")  # Consume '('
            self.expression()  # Parse the inner expression
            self.consume("RPAREN")  # Consume ')'
        else:
            self.error(f"Unexpected token: {self.current_token}")

    def match(self, token_type, value=None):
        """
        Check if the current token matches the given type (and optionally value).
        """
        if self.is_at_end():
            return False
        if self.current_token[1] == token_type:
            if value is None or self.current_token[0] == value:
                return True
        return False

    def consume(self, expected_type, expected_lexeme=None):
        """
        Consumes the current token if it matches the expected type (and optionally the expected lexeme).
        """
        if self.is_at_end():
            self.error(f"Unexpected end of input. Expected {expected_type}.")

        actual_type, actual_lexeme, line = self.current_token[1], self.current_token[0], self.current_token[2]

        if actual_type == expected_type and (expected_lexeme is None or actual_lexeme == expected_lexeme):
            print(f"Consumed token: {self.current_token}")
            self.current_index += 1
            if self.current_index < len(self.tokens):
                self.current_token = self.tokens[self.current_index]
            else:
                self.current_token = None
        else:
            expected = f"{expected_type} ('{expected_lexeme}')" if expected_lexeme else expected_type
            actual = f"{actual_type} ('{actual_lexeme}')"
            self.error(f"Expected {expected}, but found {actual} on line {line}.")

    def advance(self):
        """
        Move to the next token.
        """
        if not self.is_at_end():
            self.current_index += 1
            self.current_token = self.tokens[self.current_index] if not self.is_at_end() else None

    def is_at_end(self):
        """
        Check if the parser has reached the end of the token list.
        """
        return self.current_index >= len(self.tokens)

    def error(self, message):
        """Handles syntax errors and includes line information."""
        if self.current_token:
            lexeme, token_type, line_number = self.current_token
            raise ValueError(
                f"Syntax Error at line {line_number}: {message} "
                f"(Token: '{lexeme}', Type: '{token_type}')"
            )
        else:
            raise ValueError(f"Syntax Error: {message}")
    