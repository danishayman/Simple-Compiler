import os
from lexer import *
from parser import *

# Directory containing test case files
test_cases_dir = "test_cases"

# Postfix Converter Class
class ParseTreeConverter:
    def _init_(self):
        self.precedence = {
            '+': 1, '-': 1, 
            '*': 2, '/': 2, '%': 2
        }
        self.comparison_ops = {'<', '>', '<=', '>=', '==', '!='}

    def convert_to_parse_tree(self, tokens):
        """
        Convert tokens to a parse tree representation.
        """
        parse_tree = []
        operator_stack = []

        for token in tokens:
            lexeme, token_type, _ = token
            
            if token_type in ('INTEGER', 'IDENTIFIER'):
                parse_tree.append(lexeme)
            
            elif lexeme == '(':
                operator_stack.append(lexeme)
            
            elif lexeme == ')':
                while operator_stack and operator_stack[-1] != '(':
                    parse_tree.append(operator_stack.pop())
                
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
            
            elif token_type in ('ARITHMETIC', 'COMPARISON', 'EQUALITY'):
                while (operator_stack and operator_stack[-1] != '(' and 
                       (lexeme in self.comparison_ops or 
                        (lexeme in self.precedence and 
                         self.precedence.get(operator_stack[-1], 0) >= self.precedence.get(lexeme, 0)))):
                    parse_tree.append(operator_stack.pop())
                operator_stack.append(lexeme)
        
        while operator_stack:
            parse_tree.append(operator_stack.pop())
        
        return parse_tree

# Function to run lexer and parser on each test case file
def run_test_case(file_path):
    print("\n")
    print(f"\033[93mRunning test case: {file_path}...\033[0m")
    
    # Read the source code from the test case file
    with open(file_path, 'r') as file:
        source_code = file.read()
    
    converter = ParseTreeConverter()
    
    try:
        tokens = tokenize(source_code)  # Run the lexer
        display_tokens(tokens)
        print("\n" + "=" * 40 + "\n")
        Parser(tokens)  # Run the parser
        
        # Convert expressions to parse tree if parsing succeeds
        expression_tokens = [
            token for token in tokens 
            if token[1] in ('INTEGER', 'IDENTIFIER', 'ARITHMETIC', 'COMPARISON', 'EQUALITY', 'LPAREN', 'RPAREN')
        ]
        
        if expression_tokens:
            parse_tree = converter.convert_to_parse_tree(expression_tokens)
            print("\033[94mParse Tree:\033[0m")
            for i, node in enumerate(parse_tree, 1):
                print(f"{node}")
        
        print(f"\033[92mTest case {file_path} passed.\033[0m")
    except ValueError as e:
        print(f"\033[91mLexer error in {file_path}: {e}\033[0m")
    except SyntaxError as e:
        print(f"\033[91mSyntax error in {file_path}: {e}\033[0m")
    except Exception as e:
        print(f"\033[91mUnexpected error in {file_path}: {e}\033[0m")

# Get all test case files in the test_cases directory
test_case_files = [f for f in os.listdir(test_cases_dir) if f.endswith('.txt')]

# Run all test cases
for test_case_file in test_case_files:
    test_case_path = os.path.join(test_cases_dir, test_case_file)
    run_test_case(test_case_path)
