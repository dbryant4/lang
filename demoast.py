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
