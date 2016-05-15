import ply.lex as lex

tokens = (
    'NAME',
    'NUMBER',
    'PLUS',
    'MINUS',
    'EQUAL',
    'PLUSEQUAL',
    'MINUSEQUAL',
    'SEMICOLON',
)

t_NAME = r'[a-z]+'
t_NUMBER = r'\d+'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_EQUAL = r'\='
t_PLUSEQUAL = r'\+\='
t_MINUSEQUAL = r'\-\='
t_SEMICOLON = r'\;'

t_ignore = ' '

def t_error(t):
    raise Exception('LexerException: ' + t.value[0])

lex.lex()
