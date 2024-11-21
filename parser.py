class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def match(self, expected_type):
        token = self.current_token()
        if token and token[1] == expected_type:
            self.pos += 1
            return token
        return None

    def parse(self):
        return self.parse_program()

    def parse_program(self):
        return self.parse_statement_list()

    def parse_statement_list(self):
        statements = []
        while self.current_token() and self.current_token()[0] != "}":
            statements.append(self.parse_statement())
        return {"type": "StatementList", "statements": statements}

    def parse_statement(self):
        if self.match("KEYWORD"):
            keyword = self.tokens[self.pos - 1][0]
            if keyword == "if":
                return self.parse_if_statement()
            elif keyword == "print":
                return self.parse_output()
            # Handle other keywords like 'while', 'for', etc.
            # ... 
        elif self.match("IDENTIFIER"):
            return self.parse_assignment()
        self.error("Expected a statement.")

    def parse_assignment(self):
        identifier = self.tokens[self.pos - 1]
        if not self.match("ASSIGNMENT"):
            self.error("Expected '=' in assignment.")
        expr = self.parse_expression()
        if not self.match("SEMICOLON"):
            self.error("Expected ';' at the end of assignment.")
        return {"type": "Assignment", "identifier": identifier[0], "expression": expr}

    def parse_if_statement(self):
        if self.current_token()[0] != "(":
            self.error("Expected '(' after 'if'.")
        self.pos += 1  # Consume the '('
        condition = self.parse_expression()
        if self.current_token()[0] != ")":
            self.error("Expected ')' after condition.")
        self.pos += 1  # Consume the ')'
        if_block = self.parse_block()
        else_block = None
        if self.match("KEYWORD") and self.tokens[self.pos - 1][0] == "else":
            else_block = self.parse_block()
        return {"type": "IfStatement", "condition": condition, "if_block": if_block, "else_block": else_block}

    def parse_output(self):
        if self.current_token()[0] != "(":
            self.error("Expected '(' after 'print'.")
        self.pos += 1  # Consume the '('
        expr = self.parse_expression()
        if self.current_token()[0] != ")":
            self.error("Expected ')' after expression.")
        self.pos += 1  # Consume the ')'
        if not self.match("SEMICOLON"):
            self.error("Expected ';' after 'print'.")
        return {"type": "Output", "expression": expr}

    def parse_block(self):
        if self.current_token()[0] != "{":
            self.error("Expected '{' for block.")
        self.pos += 1  # Consume the '{'
        statements = self.parse_statement_list()
        if self.current_token()[0] != "}":
            self.error("Expected '}' to close block.")
        self.pos += 1  # Consume the '}'
        return statements

    def parse_expression(self):
        left = self.parse_term()
        while self.current_token() and self.current_token()[1] == "ARITHMETIC" and self.current_token()[0] in "+-":
            operator = self.current_token()[0]
            self.pos += 1
            right = self.parse_term()
            left = {"type": "BinaryExpression", "operator": operator, "left": left, "right": right}

        if self.current_token() and self.current_token()[1] == "COMPARISON":
            operator = self.current_token()[0]
            self.pos += 1
            right = self.parse_term()  
            left = {"type": "BinaryExpression", "operator": operator, "left": left, "right": right}

        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.current_token() and self.current_token()[1] == "ARITHMETIC" and self.current_token()[0] in "*/":
            operator = self.current_token()[0]
            self.pos += 1
            right = self.parse_factor()
            left = {"type": "BinaryExpression", "operator": operator, "left": left, "right": right}
        return left

    def parse_factor(self):
        token = self.current_token()
        if token[1] == "INTEGER":
            self.pos += 1
            return {"type": "Literal", "value": int(token[0]), "datatype": "int"}  # Add datatype
        elif token[1] == "FLOAT":  # Handle float literals
            self.pos += 1
            return {"type": "Literal", "value": float(token[0]), "datatype": "float"}  # Add datatype
        elif token[1] == "STRING":  # Handle string literals
            self.pos += 1
            return {"type": "Literal", "value": token[0][1:-1], "datatype": "string"}  # Add datatype
        elif token[1] == "BOOLEAN":  # Handle boolean literals
            self.pos += 1
            return {"type": "Literal", "value": token[0] == 'true', "datatype": "bool"}  # Add datatype
        elif token[1] == "IDENTIFIER":
            self.pos += 1
            return {"type": "Variable", "name": token[0]}
        elif token[1] == "LAPREN":
            self.pos += 1
            expr = self.parse_expression()
            if self.current_token()[0] != ")":
                self.error("Expected ')' to close expression.")
            self.pos += 1  # Consume the ')'
            return expr
        self.error("Unexpected token in factor.")

    def error(self, message):
        token = self.current_token()
        raise ValueError(f"Syntax error at token {token}: {message}")