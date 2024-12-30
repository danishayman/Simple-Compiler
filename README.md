# 🖥️ MiniLang

This project is a simple compiler implemented in Python, consisting of a lexer, parser, and parse tree converter. It tokenizes input code, parses it into an abstract syntax tree (AST), and checks for syntax correctness.

---

## 📜 Features

- **Lexer**: Tokenizes input code based on predefined patterns.
- **Parser**: Parses tokens into an abstract syntax tree and checks syntax correctness.
- **Parse Tree Converter**: Converts expressions into a parse tree for postorder traversal.
- **Error Handling**: Provides meaningful errors for unexpected characters or syntax issues.
- **Test Automation**: Runs test cases to validate the compiler's functionality.

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/danishayman/Simple-Compiler.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Simple-Compiler
   ```
3. Ensure Python is installed (version 3.8 or later).



---

## 🚀 Usage

1. Place your test case files in the `test_cases` directory.
2. Run the `main.py` script to execute the lexer, parser, and tree converter on all test cases:
   ```bash
   python main.py
   ```
3. Check the console output for tokenized results, parse trees, and syntax analysis.

---

## 🛠️ File Structure

- `main.py`: Entry point of the project.
- `lexer.py`: Contains the lexer implementation.
- `parser.py`: Contains the parser and syntax error handling.
- `constant.py`: Defines token patterns used by the lexer.
- `test_cases/`: Directory for test case files.

---

## 🧪 Example Test Case

**Input:**
```python
int x = 5;
if (x < 10) {
    print(x);
}
```

**Output:**
```plaintext
Lexemes         Tokens          Line
-------------  -------------  -----
int            KEYWORD        1
x              IDENTIFIER     1
=              ASSIGNMENT     1
5              INTEGER        1
;              SEMICOLON      1
if             KEYWORD        2
(              LPAREN         2
x              IDENTIFIER     2
<              COMPARISON     2
10             INTEGER        2
)              RPAREN         2
{              LBRACE         3
print          KEYWORD        3
(              LPAREN         3
x              IDENTIFIER     3
)              RPAREN         3
;              SEMICOLON      3
}              RBRACE         4

Abstract Syntax Tree in Postorder Traversal:
x
5
<
print
```

---

## 📝 Contributions

Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

---

