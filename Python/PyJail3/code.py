#!/usr/bin/python
# flag{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}
import pickle
import base64

def print_history(state):
    print 'Count: ' + str(len(state))
    for key in state:
        print key + ' = ' + str(state[key])

def export_state(state):
    print 'Your state: '+base64.b64encode(pickle.dumps(state))

def import_state(encoded_state):
    global state
    state = pickle.loads(base64.b64decode(encoded_state))

def evaluate(expr, state):
    for c in expr:
        if c not in whitelist:
            print("Go away!")
            exit(0)

    result = eval(expr)
    state[expr] = result
    print(expr + " = " + str(result))

print("Calculator v0.2")

whitelist = '0123456789.+-*/^%()&| '

menu = '''calc <expr> - evaluate expression
import <state> - load your state
export - print current encoded state
history - print your history
quit - exit from application'''

state = {}

while True:
    print menu
    choice = raw_input('> ')
    if choice == 'export':
        export_state(state)
        continue
    elif choice == 'quit':
        exit(0)
    elif choice == 'history':
        print_history(state)
        continue

    if ' ' not in choice:
        print 'Invalid command'
        continue

    command, arg = choice.split(' ', 1)
    if command == 'import':
        import_state(arg)
    elif command == 'calc':
        evaluate(arg, state)
    else:
        print 'Invalid command'
