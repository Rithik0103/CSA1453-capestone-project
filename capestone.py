from ply import lex, yacc

# Define tokens
tokens = (
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Define token regex
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Define a rule to handle identifiers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Define a rule to handle numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignore whitespace
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Define the grammar
def p_expression_binop(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
    '''
    # Do something with the parsed expression

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# Main function for input and parsing
def main():
    while True:
        try:
            s = input('>>> ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(result)

if __name__ == '__main__':
    main()
