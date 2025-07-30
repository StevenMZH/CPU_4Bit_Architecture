
RAM16x12B = [ [0]*12 for i in range(16) ]

def RAM_Management(direction, data = 0, write = 0, reset = 0, writeData = 0):

    global RAM16x12B

    direction = ''.join(map(str,(direction)))
    direction = int(direction, 2 )
    out = [0]*12
    
    # Read
    if(write == 0):
        print(RAM16x12B[direction])
        out = RAM16x12B[direction]

    # Write
    elif(write == 1):
        RAM16x12B[direction] = data
        print(RAM16x12B[direction])
        out = RAM16x12B[direction]

    if(writeData == 1):
        RAM16x12B[direction] = [1,1,0,0, data[0],data[1],data[2],data[3], 0,0,0,0]
        print(RAM16x12B[direction])

    # Reset
    if (reset == 1):
        RAM16x12B = [ [0]*12 for i in range(16) ]

    return out

def printRAM():
    print()
    n = 0
    for i in RAM16x12B:
        print (f"{n}\t\t{i[0]}{i[1]}{i[2]}{i[3]}\t {i[4]}{i[5]}{i[6]}{i[7]}\t {i[8]}{i[9]}{i[10]}{i[11]}\t")

        if((n+1)%4 == 0):
            print()

        n +=1

    print()

def LoadProgram(code):
    global RAM16x12B

    if(len(RAM16x12B) == len(code) and len(RAM16x12B[0]) == len(code[0]) ):
        RAM16x12B = code

    return code



multiplication = [
                    # Variable Initialization
                  [1,0,1,0,  0,0,1,0,  0,0,0,0], # mov  r2,  0           # r2 = 0
                  [1,0,0,1,  1,1,0,1,  0,0,0,1], # mov  R13, r1          # R13 = r1
                  [1,0,1,0,  0,0,1,1,  0,0,0,1], # mov  r3,  1           # r3 = 1

                    # Calculations
                  [0,1,0,0,  1,1,1,0,  0,0,0,0], # sum  R14, r0          # r2 = R14 + r0
                  [1,0,0,1,  1,1,1,0,  0,0,1,0], # mov  R14, r2          # R14 = r2
                  [0,1,0,1,  1,1,0,1,  0,0,1,1], # sub  R13, r3          # r2 = R13 - r3
                  [1,0,0,1,  1,1,0,1,  0,0,1,0], # mov  R13, r2          # R13 = r2

                    # Do while
                  [1,1,0,1,  0,0,1,1,  0,0,1,0], # jmp! R3,  r2          # Jump to R3, if(r2 != R15)

                    # Result
                  [1,0,1,1,  0,0,1,0,  1,1,1,0], # mov r2, R14           # r2 = R14
                  [1,1,1,0,  0,0,0,0,  0,0,0,0], # Stop                  # return void

                    # Skip
                  [1,1,0,0,  0,0,0,0,  0,0,0,0], # int  0
                  [1,1,0,0,  0,0,0,0,  0,0,0,0], # int  0
                  [1,1,0,0,  0,0,0,0,  0,0,0,0], # int  0

                    # Variables
                  [1,1,0,0,  0,0,0,0,  0,0,0,0], # int  0                # Down Counter
                  [1,1,0,0,  0,0,0,0,  0,0,0,0], # int  0                # Mult
                  [1,1,0,0,  0,0,0,0,  0,0,0,0]  # int  0                # Jump Condition
                
]

Reseted = [ [0]*12 for i in range(16) ]



