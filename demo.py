import demoparse

data = {}
demoparse.parse('x = 1; x += 1; y = 4 - x; x -= y;').interpret(data)
print(data)
