# MiniLang.py



class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0
        self.tokens = []
        self.tokenize()

    def advance(self):
        self.position += 1

    def tokenize(self):
        while self.position < len(self.code):
            char = self.code[self.position]
            if char.isalpha():  # Check for identifiers/keywords
                token = self.read_keyword_or_identifier()
                self.tokens.append(('IDENTIFIER', token))
            elif char.isdigit():  # Check for numbers
                token = self.read_number()
                self.tokens.append(('NUMBER', token))
            elif char in '+-*/=':  # Check for operators
                self.tokens.append(('OPERATOR', char))
                self.advance()
            else:
                self.advance()

    def read_keyword_or_identifier(self):
        start = self.position
        while self.position < len(self.code) and self.code[self.position].isalnum():
            self.advance()
        return self.code[start:self.position]

    def read_number(self):
        start = self.position
        while self.position < len(self.code) and self.code[self.position].isdigit():
            self.advance()
        return self.code[start:self.position]






class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        # Start parsing by looking for expressions
        return self.expression()

    def expression(self):
        # Implement the expression logic
        pass

    def term(self):
        #Implement the term logic
        pass

    def evaluate(self, left, operator, right):
        #Implement the evaluation logic
        pass







class SemanticAnalyzer:
    def __init__(self, ast):
        self.ast = ast
        self.symbol_table = {}

    def analyze(self):
        # Implement semantic analysis logic
        pass
