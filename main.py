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
        tokens = tokenize(source_code)  # Run the lexer
        display_tokens(tokens)
        print("\n" + "=" * 40 + "\n")
        Parser(tokens)  # Run the parser
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
