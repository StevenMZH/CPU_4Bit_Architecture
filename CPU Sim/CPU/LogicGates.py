
# Basic Gates

def AND(a:int, b:int):
    if(a == b == 1):
        return 1
    elif(a == 0 or b == 0):
        return 0
    return -1

def OR(a:int, b:int):
    if(a == 1 or b == 1):
        return 1
    elif(a == b == 0):
        return 0
    return -1

def NOT(a:int):
    if(a == 1):
        return 0
    elif(a == 0):
        return 1
    return -1

# Compuest Gates

def NAND(a:int, b:int):
    return NOT( AND(a,b) )

def NOR(a:int, b:int):
    return NOT( OR(a,b) )

def XOR(a:int, b:int):
    return OR( AND( a,NOT(b) ), AND(NOT(a), b))

def XNOR(a:int, b:int):
    return NOT( XOR(a,b) )





