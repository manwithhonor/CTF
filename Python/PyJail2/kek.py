#!/usr/bin/python
# flag{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}

print("Calculator v0.1")

expr = raw_input("expression = ")

bad_words = ['import', 'eval', 'exec', 'os', 'sys', 'input', 'open', '_']

for bad_word in bad_words:
    if bad_word in expr:
        print("Go away!")
        exit(0)

print(expr + " = " + str(eval(expr)))
