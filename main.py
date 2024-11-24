import os
from lexer import *
from parser import *

# Directory containing test case files
test_cases_dir = "test_cases"

# Function to run lexer and parser on each test case file
def run_test_case(file_path):
    print(f"Running test case: {file_path}")
    print("\n")
    
    # Read the source code from the test case file
    with open(file_path, 'r') as file:
        source_code = file.read()
    
    try:
        # Run the lexer to generate tokens from the source code
        tokens = tokenize(source_code)
        
        # Display the generated tokens
        display_tokens(tokens)
        print("\n" + "="*40 + "\n")
        
        # Run the parser on the tokens to check for syntax correctness
        Parser(tokens)
        print(f"Test case {file_path} passed.\n")
    except SyntaxError as e:
        # Handle syntax errors encountered during parsing
        print(f"Syntax error in {file_path}: {e}")
    except ValueError as e:
        # Handle lexer errors encountered during tokenization
        print(f"Lexer error in {file_path}: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Unexpected error in {file_path}: {e}")
    finally:
        # Print a separator for readability between test cases
        print("\n" + "="*40 + "\n")

# Get all test case files in the test_cases directory
test_case_files = [f for f in os.listdir(test_cases_dir) if f.endswith('.txt')]

# Run all test cases
for test_case_file in test_case_files:
    test_case_path = os.path.join(test_cases_dir, test_case_file)
    run_test_case(test_case_path)
