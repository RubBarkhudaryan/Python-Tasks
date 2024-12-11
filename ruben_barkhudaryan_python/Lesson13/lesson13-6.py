print("Built-in functions.")
print("Turning string into executable code and executing it.")

codeStr = "x = 5\ny = 10\nprint('x + y = ', x + y)"
code = compile(codeStr, "sum.py", 'exec')
print(type(code))
exec(code)