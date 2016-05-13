class Prog:
    def __init__(self, stmts):
        self.stmts = stmts
    def interpret(self, data):
        for stmt in self.stmts:
            stmt.interpret(data)

class Assign:
    def __init__(self, op, name, expr):
        self.op = op
        self.name = name
        self.expr = expr
    def interpret(self, data):
        data[self.name] = {
            '=': lambda: self.expr.interpret(data),
            '+=': lambda: data[self.name] + self.expr.interpret(data),
            '-=': lambda: data[self.name] - self.expr.interpret(data),
        }[self.op]()

class BinOp:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right
    def interpret(self, data):
        return {
            '+': lambda: self.left.interpret(data) + self.right.interpret(data),
            '-': lambda: self.left.interpret(data) - self.right.interpret(data),
        }[self.op]()

class Num:
    def __init__(self, value):
        self.value = value
    def interpret(self, data):
        return int(self.value)

class Var:
    def __init__(self, name):
        self.name = name
    def interpret(self, data):
        return data[self.name]

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

import ply.lex as lex
lexer = lex.lex()

precedence = (
    ('left', 'PLUS', 'MINUS', ),
)

def p_prog(t):
    ''' prog : stmts '''
    t[0] = Prog(t[1])

def p_stmts(t):
    ''' stmts : stmt
              | stmts stmt '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[2]]

def p_stmt(t):
    ''' stmt : assign SEMICOLON '''
    t[0] = t[1]

def p_assign(t):
    ''' assign : NAME EQUAL expr
               | NAME PLUSEQUAL expr
               | NAME MINUSEQUAL expr '''
    t[0] = Assign(t[2], t[1], t[3])

def p_expr_binop(t):
    ''' expr : expr PLUS expr
             | expr MINUS expr '''
    t[0] = BinOp(t[2], t[1], t[3])

def p_expr_number(t):
    ''' expr : NUMBER '''
    t[0] = Num(t[1])

def p_expr_name(t):
    ''' expr : NAME '''
    t[0] = Var(t[1])

def p_error(t):
    raise Exception('ParserException')

import ply.yacc as yacc
parser = yacc.yacc()
data = {}
parser.parse('x = 1; x += 1; y = 4 - x; x -= y;').interpret(data)
print(data)
