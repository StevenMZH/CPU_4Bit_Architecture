
from LogicGates import AND, OR, NOT, XOR

# Logic Unit
    
def AndBitwise_4B(A:list, B:list):
    R = [AND(A[i], B[i]) for i in range(4)]
    return R
    
def OrBitwise_4B(A:list, B:list):
    R = [OR(A[i], B[i]) for i in range(4)]
    return R

def NotBitwise_4B(A:list):
    R = [NOT(A[i]) for i in range(4)]
    return R

def LogicUnit(A:list, B:list, Op:list):

    if(Op[0] == 0 and Op[1] == 0):
        return AndBitwise_4B(A,B)
    
    elif(Op[0] == 0 and Op[1] == 1):
        return OrBitwise_4B(A,B)

    elif(Op[0] == 1 and Op[1] == 0):
        return NotBitwise_4B(A)
    
    elif(Op[0] == 1 and Op[1] == 1):
        return NotBitwise_4B(B)

    return -1

# Aritmetic Unit

def FullAdder(a:int, b:int, Cin:int):

    S = XOR(Cin, XOR(a, b))
    Cout = OR( AND(a,b) , AND( XOR(a,b), Cin))

    return [Cout, S]

def Adder4B(A:list, B:list, Cin:int = 0):
    
    S = [0, 0, 0, 0]
    Overflow = 0
    bit = [Cin, 0]

    for i in range(3, -1, -1):
        bit = FullAdder(A[i], B[i], bit[0])
        S[i] = bit[1] 

    S.insert(0, bit[0]) 

    return S

def Substracter(A:list, B:list, Op:int):
    if(Op == 0):
        return Adder4B(A,B)
    
    elif(Op == 1):
        return Adder4B(A, NotBitwise_4B(B), 1)
    
    else:
        return -1
        
def ArithmeticUnit(A:list, B:list, Op:list):

    if(Op[0] == 0):
        return Substracter(A,B,Op[1])

    elif(Op[0] == 1 and Op[1] == 1):
        return Substracter(B, A, 1)
    
    elif(Op[0] == 1 and Op[1] == 0):
        return Adder4B(A, [0,0,0,1])
    
# Comparator
    
def Comparator4B(A:list, B:list):

    for i in range(4):
        if(A[i] > B[i]):
            return [1,0,0]

        elif(A[i] < B[i]):
            return [0,0,1]
    
    return [0,1,0]

    
# ALU

def ALU(A:list, B:list, Op:list):

    # Comparator
    relationalData = Comparator4B(A, B)

    # Logic Unit
    if(Op[0] == 0):
        R = LogicUnit(A,B,[Op[1], Op[2]])

        DataType = [0,0,0]
    
        return DataType,R,relationalData

    # Arithmetic Unit
    elif(Op[0] == 1):
        aux = ArithmeticUnit(A,B,[Op[1], Op[2]])
        R = aux[1:]
        negative = 0
        
        if( (relationalData[2] == 1 and Op[1] == 0 and Op[2] == 1) or (relationalData[0] == 1 and Op[1] == 1 and Op[2] == 1) ):
            negative = 1

        if( (Op[1] == 0 and Op[2] == 1) or (Op[1] == 1 and Op[2] == 0) ):
            aux[0] = 0

            if(R[0] == 0 and negative == 1):
                aux[0] = 1
                    
        DataType = [aux[0], 1, negative]

        return DataType,R,relationalData

    return -1

