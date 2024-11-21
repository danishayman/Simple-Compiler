import os
from lexer import tokenize, print_tokens
from parser import Parser
from ast_visualizer import visualize_ast

# Directory containing test case files
test_cases_dir = "test_cases"

# Function to run lexer and parser on each test case file
def run_test_case(file_path):
    print(f"Running test case: {file_path}")
    
    # Read source code from the file
    with open(file_path, 'r') as file:
        source_code = file.read()
    
    # Tokenize the source code using the tokenize function
    try:
        tokens = tokenize(source_code)
        print_tokens(tokens)

        # Create Parser and generate AST
        parser = Parser(tokens)  # Create a Parser instance 
        ast = parser.parse()     # Now you can use the parser
        visualize_ast(ast)

    except ValueError as e:
        print(f"Error processing {file_path}: {e}")
    print("\n" + "="*40 + "\n")

# Get all test case files in the test_cases directory
test_case_files = [f for f in os.listdir(test_cases_dir) if f.endswith('.txt')]

# Run all test cases
for test_case_file in test_case_files:
    test_case_path = os.path.join(test_cases_dir, test_case_file)
    run_test_case(test_case_path)