
from ALU import ALU
from RAM import RAM16x12B,RAM_Management, printRAM, LoadProgram, multiplication, Reseted
from Cache import Cache8x4B, Cache_Management, printCache

LineCounter = 0


def IRT_Processing(code):

    global LineCounter
    global Cache8x4B
    global RAM16x12B

    Op = code[0:4]
    A = code[4:8]
    B = code[8:12]

    strA = ''.join(map(str, A))
    strB = ''.join(map(str, B))
    
    RA = RAM16x12B[int(strA,2)]; RA = RA[4:8]
    RB = RAM16x12B[int(strB,2)]; RB = RB[4:8]

    # ALU
    if(Op[0] == 0):
        
        a,AUX,a2 = ALU(A,B, Op[1:])
        print(a,AUX,a2)
        print()
        Cache_Management(QA = 1, r2W = 1, r2 = AUX)

    elif(Op[0] == 1):

        # Storage
        if(Op[1] == 0 and Op[2] == 0):
            # RAM Asignation

            if(Op[3] == 0):
                RAM_Management(A,B, writeData=1)
                print()

            elif(Op[3] == 1):
                rB = Cache8x4B[int(strB,2)]
                RAM_Management(A,rB, writeData=1)
                print()

        elif(Op[1] == 0 and Op[2] == 1):

            # Cache Assignation
            if(Op[3] == 0):
                Cache_Management(A, B, write = 1)

            elif(Op[3] == 1):
                Cache_Management(A, RB, write = 1)

        # Special Commands

        elif(Op[1] == 1):
    
            strA = ''.join(map(str, A))
            
            if(Op[2] == 0 and Op[3] == 0):
                Cache_Management(A)

            elif(Op[2] == 0 and Op[3] == 1):
                Cache_Management(reset=1)

            elif(Op[2] == 1 and Op[3] == 0):
                Cache_Management(QA=1, r0=A, r0W=1, r1=B, r1W=1)

            elif(Op[2] == 1 and Op[3] == 1):
                LineCounter = int(strA,2)

        else:
            return -1
        
def Execute():

    global LineCounter
    global RAM16x12B
    global Cache8x4B

    while(LineCounter <= 15):
    
        code = RAM16x12B[LineCounter]
        
        Op = code[0:4]
        
        A = code[4:8]
        B = code[8:12]

        strA = ''.join(map(str, A))
        strB = ''.join(map(str, B))

        RA = RAM16x12B[int(strA,2)]; RA = RA[4:8]
        RB = RAM16x12B[int(strB,2)]; RB = RB[4:8]
        R15 = RAM16x12B[-1]; R15 = R15[4:8]


        # ALU
        if(Op[0] == 0):
            rB = Cache8x4B[int(strB,2)]
            a,AUX,a2 = ALU(RA,rB, Op[1:])
            Cache_Management(QA = 1, r2W = 1, r2 = AUX)

        elif(Op[0] == 1):

            # Storage
                    
            if(Op[1] == 0 and Op[2] == 0):
                # RAM Asignation

                if(Op[3] == 0):
                    RAM_Management(A,B, writeData=1)

                elif(Op[3] == 1):
                    rB = Cache8x4B[int(strB,2)]
                    RAM_Management(A,rB, writeData=1)
            
            elif(Op[1] == 0 and Op[2] == 1):

                # Cache Assignation
                if(Op[3] == 0):
                    Cache_Management(A, B, write = 1)

                elif(Op[3] == 1):
                    Cache_Management(A, RB, write = 1)

            # Special Commands

            elif(Op[1] == 1):
                
                if(Op[2] == 0 and Op[3] == 0):
                    pass #Skip (Data Loaded, Not Code)

                elif(Op[2] == 0 and Op[3] == 1):
                    rB = Cache8x4B[int(strB,2)]

                    if(R15 != rB): #JUMP!
                        LineCounter = int(strA, 2)

                        continue

                elif(Op[2] == 1 and Op[3] == 0):
                    break # STOP

                elif(Op[2] == 1 and Op[3] == 1):
                    rB = Cache8x4B[int(strB,2)]

                    if(R15 == rB): #JUMP
                        LineCounter = int(strA, 2)
                        continue

            else:
                return -1
            
        print("\t\t#",LineCounter,"#\t")
        printRAM()
        printCache()
        print()
        print()

        LineCounter += 1

def Programate(code,editing):
    
    global LineCounter
    global RAM16x12B
    global Cache8x4B

    if(editing == 0):
        RAM16x12B[LineCounter] = code
        LineCounter += 1
        printRAM()
        print()
        print()
        

    elif(editing == 1):
        A = code[4:8]
        strA = ''.join(map(str, A))
        LineCounter = int(strA, 2) 
        print()
        print("Line: ", LineCounter)
        print()



def CPU(program = Reseted):

    global RAM16x12B

    print("\n\n\n\tCPU (SMx4-12)\n")

    RAM16x12B = LoadProgram(program)

    while(True):

        I = str(input())
        I = I.replace(" ", "")
        I = [int(i) for i in I]
        print()

        if(len(I) == 15):

            # ON
            if(I[0] == 1):

                code = I[3:]

                # In Real Time Processing
                if(I[1] == 0 and I[2] == 0):
                    IRT_Processing(code)

                # Executable
                if(I[1] == 0 and I[2] == 1):
                    Execute()

                # Programming
                if(I[1] == 1):
                    Programate(code, I[2])
            # OFF
            else:
                break


CPU(multiplication)









