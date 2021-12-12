""" Global variable is declared outside the function"""
A=72
def glob():
    
    global A #A is a global variable

    print(A)

    """ Changing the global variable value"""
    A="Value is changed"
    print(A)
glob()
print(A)
