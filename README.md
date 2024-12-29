# MiniLang

Context-Free Grammar

program         -> statement_list

statement_list  -> statement*

statement       -> variable_declaration
                | assignment
                | if_statement
                | while_statement
                | function_definition
                | print_statement

variable_declaration -> "int" IDENTIFIER ";" 
                      | "float" IDENTIFIER ";" 

assignment      -> IDENTIFIER "=" expression ";"

if_statement    -> "if" "(" expression ")" "{" statement_list "}"

while_statement -> "while" "(" expression ")" "{" statement_list "}"

function_definition -> "def" IDENTIFIER "(" parameter_list ")" "{" statement_list "}"

parameter_list  -> IDENTIFIER ("," IDENTIFIER)*

print_statement -> "print" "(" STRING ");"

expression      -> term (( "+" | "-" ) term)*

term            -> factor (( "*" | "/" ) factor)*

factor          -> INTEGER 
                | FLOAT 
                | IDENTIFIER 
                | "(" expression ")"
