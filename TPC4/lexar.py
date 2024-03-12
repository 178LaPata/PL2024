import ply.lex as lex

tokens = (
    'SELECT',
    'VARIABLE',
    'COMMA',
    'FROM',
    'WHERE',
    'EQUAL',
    'GREATER_THAN',
    'LESS_THAN',
    'GREATER_EQUAL',
    'LESS_EQUAL',
    'NUMBER'
)

t_SELECT = r'select'
t_VARIABLE = r'[a-zA-Z]+'
t_COMMA = r','
t_FROM = r'from'
t_WHERE = r'where'
t_EQUAL = r'\='
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_GREATER_EQUAL = r'\>\='
t_LESS_EQUAL = r'\<\='
t_NUMBER = r'\d+'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Invalid character '{t.value[0]}' at position {t.lexpos}")
    t.lexer.skip(1)
    return

lexer = lex.lex()

v = """
SELECT id, nome, salario FROM empregados WHERE salario >= 820
"""

lexer.input(v)
for tok in lexer:
    print(tok)





