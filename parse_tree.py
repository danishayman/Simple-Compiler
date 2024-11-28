class ParseTree:
    def __init__(self, tokens):
        self.tokens = tokens
        self.root = None
        self.current_index = 0
        self.current_token = self.tokens[self.current_index]
        self.generate_parse_tree()

    def generate_parse_tree(self):
        self.root = self.create_program_node()

    def create_program_node(self):
        program_node = {
            "type": "Program",
            "statements": []
        }

        while self.current_index < len(self.tokens):
            statement_node = self.create_statement_node()
            if statement_node:
                program_node["statements"].append(statement_node)

        return program_node

    def create_statement_node(self):
        """
        Create a node for different types of statements.
        """
        token_type = self.current_token[1]
        
        if token_type == "IDENTIFIER":
            return self.create_assignment_node()
        elif token_type == "KEYWORD":
            lexeme = self.current_token[0]
            if lexeme == "if":
                return self.create_if_node()
            elif lexeme == "while":
                return self.create_while_node()
            elif lexeme == "print":
                return self.create_print_node()
        
        # Move to next token if no specific node is created
        self.advance()
        return None

    def create_assignment_node(self):
        """
        Create a node for assignment statements.
        """
        node = {
            "type": "AssignmentStatement",
            "variable": self.current_token[0],
            "value": None
        }
        self.advance()  # variable
        
        if self.current_token[1] == "ASSIGNMENT":
            self.advance()  # assignment operator
            
            # Create expression node
            node["value"] = self.create_expression_node()
            
            # Consume semicolon
            if self.current_token[1] == "SEMICOLON":
                self.advance()
        
        return node

    def create_expression_node(self):
        """
        Create a node for expressions.
        """
        node = {
            "type": "Expression",
            "left": self.current_token[0],
            "operator": None,
            "right": None
        }
        
        # Advance past left operand
        self.advance()
        
        # Check for arithmetic or comparison operators
        if self.current_token[1] in ("ARITHMETIC", "COMPARISON"):
            node["operator"] = self.current_token[0]
            self.advance()
            
            # Right operand
            if self.current_token:
                node["right"] = self.current_token[0]
                self.advance()
        
        return node

    def create_if_node(self):
        """
        Create a node for if statements.
        """
        node = {
            "type": "IfStatement",
            "condition": None,
            "true_node": [],
            "else_node": []
        }
        
        # Consume 'if' keyword
        self.advance()
        
        # Consume condition in parentheses
        if self.current_token[1] == "LPAREN":
            self.advance()
            node["condition"] = self.create_expression_node()
            
            # Consume right parenthesis
            if self.current_token[1] == "RPAREN":
                self.advance()
        
        # Consume left brace
        if self.current_token[1] == "LBRACE":
            self.advance()
        
        # Parse statements in true node
        while self.current_token[1] != "RBRACE":
            statement = self.create_statement_node()
            if statement:
                node["true_node"].append(statement)
        
        # Consume right brace
        self.advance()
        
        # Handle else block if present
        if (self.current_token and 
            self.current_token[1] == "KEYWORD" and 
            self.current_token[0] == "else"):
            self.advance()  # consume 'else'
            
            # Consume left brace
            if self.current_token[1] == "LBRACE":
                self.advance()
            
            # Parse statements in else node
            while self.current_token[1] != "RBRACE":
                statement = self.create_statement_node()
                if statement:
                    node["else_node"].append(statement)
            
            # Consume right brace
            self.advance()
        
        return node

    def create_while_node(self):
        """
        Create a node for while statements.
        """
        node = {
            "type": "WhileStatement",
            "condition": None,
            "block": []
        }
        
        # Consume 'while' keyword
        self.advance()
        
        # Consume condition in parentheses
        if self.current_token[1] == "LPAREN":
            self.advance()
            node["condition"] = self.create_expression_node()
            
            # Consume right parenthesis
            if self.current_token[1] == "RPAREN":
                self.advance()
        
        # Consume left brace
        if self.current_token[1] == "LBRACE":
            self.advance()
        
        # Parse statements in while block
        while self.current_token[1] != "RBRACE":
            statement = self.create_statement_node()
            if statement:
                node["block"].append(statement)
        
        # Consume right brace
        self.advance()
        
        return node

    def create_print_node(self):
        """
        Create a node for print statements.
        """
        node = {
            "type": "PrintStatement",
            "expression": None
        }
        
        # Consume 'print' keyword
        self.advance()
        
        # Consume left parenthesis
        if self.current_token[1] == "LPAREN":
            self.advance()
        
        # Create expression node
        node["expression"] = self.create_expression_node()
        
        # Consume right parenthesis
        if self.current_token[1] == "RPAREN":
            self.advance()
        
        # Consume semicolon
        if self.current_token[1] == "SEMICOLON":
            self.advance()
        
        return node

    def advance(self):
        """
        Move to the next token.
        """
        self.current_index += 1
        if self.current_index < len(self.tokens):
            self.current_token = self.tokens[self.current_index]
        else:
            self.current_token = None

    def print_parse_tree(self, node=None, indent=0):
        """
        Print the parse tree 
        """
        if node is None:
            node = self.root

        print("  " * indent + str(node.get("type", "Node")))
        
        for key, value in node.items():
            if key != "type":
                if isinstance(value, list):
                    print("  " * (indent + 1) + f"{key}:")
                    for item in value:
                        self.print_parse_tree(item, indent + 2)
                elif isinstance(value, dict):
                    print("  " * (indent + 1) + f"{key}:")
                    self.print_parse_tree(value, indent + 2)
                elif key in ["variable", "left", "right", "expression", "operator"]:
                    print("  " * (indent + 1) + f"{key}: {value}")