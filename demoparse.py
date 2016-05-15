import ply.yacc as yacc
import demolex
import demoast as ast

tokens = demolex.tokens

precedence = (
    ('left', 'PLUS', 'MINUS', ),
)

def p_prog(t):
    ''' prog : stmts '''
    t[0] = ast.Prog(t[1])

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
    t[0] = ast.Assign(t[2], t[1], t[3])

def p_expr_binop(t):
    ''' expr : expr PLUS expr
             | expr MINUS expr '''
    t[0] = ast.BinOp(t[2], t[1], t[3])

def p_expr_number(t):
    ''' expr : NUMBER '''
    t[0] = ast.Num(t[1])

def p_expr_name(t):
    ''' expr : NAME '''
    t[0] = ast.Var(t[1])

def p_error(t):
    raise Exception('ParserException')

parser = yacc.yacc()

def parse(data):
    parser.error = 0
    p = parser.parse(data)
    if parser.error: return None
    return p
