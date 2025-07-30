
Cache8x4B = [ [0]*4 for i in range(8) ]

def Cache_Management(direction = [0,0,0,0], data = 0, write = 0, reset = 0, QA = 0, r0 = 0, r0W = 0, r1 = 0, r1W = 0, r2 = 0, r2W = 0):

    global Cache8x4B

    direction = ''.join(map(str,(direction)))
    direction = int(direction, 2 )
    out = [0,0,0,0]

    # Read
    if(write == 0 and QA == 0):
        print(Cache8x4B[direction])
        print()

    # Write
    elif(write == 1 and QA == 0):
        Cache8x4B[direction] = data
        print(Cache8x4B[direction])
        print()

        out[3] = Cache8x4B[direction]

    # Quick Access

    elif(QA == 1):
        if(r0W == 1):
            Cache8x4B[0] = r0
            out[0] = Cache8x4B[0]

        if(r1W == 1):
            Cache8x4B[1] = r1
            out[1] = Cache8x4B[1]

        if(r2W == 1):
            Cache8x4B[2] = r2
            out[2] = Cache8x4B[2]

    # Reset
    if (reset == 1):
        Cache8x4B = [ [0]*4 for i in range(8) ]
        
    return out

def printCache():
    for i in Cache8x4B:
        print (i)



