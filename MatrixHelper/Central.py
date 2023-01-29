
def buffer(x):
    for i in range(x):
        print("\n")

def asker(x):

    demenAr = [[0 for i in range(x)] for e in range(2)]


    for i in range(x):
        demenAr[0][i] = (int(input("What is the width of matrix " + str(i + 1) + " \n")))
        demenAr[1][i] = (int(input("What is the height of matrix " + str(i + 1) + " \n")))

    return demenAr

def matAsk(height, width, N):
    M = [[0 for i in range(width)] for e in range(height)]
    
    for i in range(height):
        for e in range(width):
            M[i][e] = float(input("please enter element " + str(e + 1) + ", " + str(i + 1) + " for Matrix " + str(N) + "\n"))

    return M

def printMat(M, height, width):
    for e in range(height):
        print("\n")
        for i in range(width):
            print(str(M[e][i]) + " ", end="")

def idM(dem):
    ident = [[0 for i in range(dem)] for e in range(dem)]

    for i in range(dem):
        for e in range(dem):
            if i == e:
                ident[i][e] = 1
    
    return ident


def mReduce(M, ind):
    N = len(M)
    redM = [[0 for i in range(N - 1)] for e in range(N - 1)]

    adder = 0

    for i in range(N):

        if i != ind:

            for e in range(N - 1):
                redM[e][i + adder] = M[e + 1][i]
                
        else:
            adder = -1

    return redM


def twoXtwo(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def recDet(M):
    det = 0

    N = len(M)
    sign = 1

    if N > 2:
        for i in range(N):
            det += (sign) * recDet(mReduce(M, i)) * M[0][i]
            sign *= -1
    else:
        det += twoXtwo(M)

    return det    


operation = input("Hello which operation would you like to do, find the transverse, find the inverse, multiply two matrices (enter: T,I or M) \n")

if operation == "T":
    
    dem = asker(1)

    width = dem[0][0]
    height = dem[1][0]

    M = matAsk(height, width, "")

    Mtran = [[0 for i in range(height)] for e in range(width)]


    for e in range(height):
        for i in range(width):
            Mtran[i][e] = M[e][i]

    printMat(M, height, width)

    buffer(1)

    printMat(Mtran, width, height)

    buffer(2)

elif operation == "I":
    
    dem = asker(1)

    width = dem[0][0]
    height = dem[1][0]

    M = matAsk(height, width, 1)

    if recDet(M) == 0:

        print("Your matrix has a determinant equivivant to zero and therefore has no inverse")

    else:
        inv = idM(height)
        
        for j in range(height):
            for i in range(height):
                if i != j:
                    factor = M[i][j]/M[j][j]
                    
                    for e in range(height):
                        M[i][e] = M[i][e] - (M[j][e] * factor)
                        inv[i][e] = inv[i][e] - (inv[j][e] * factor)

        
        for i in range(height):
            factor = M[i][i]
            for j in range(height):
                inv[i][j] = inv[i][j]/factor
        

        printMat(M, height, width)

        buffer(1)

        printMat(inv, height, width)

elif operation == "M":
    
    dem = asker(2)

    width1 = dem[0][0]
    height1 = dem[1][0]

    width2 = dem[0][1]
    height2 = dem[1][1]

    mat1 = matAsk(height1, width1, 1)

    mat2 = matAsk(height2, width2, 2)

    matMul = [[0 for i in range(width2)] for e in range(height1)]


    for i in range(height1):
        for e in range(width2):
            
            sum = 0

            for j in range(width1):
                sum += mat1[i][j] * mat2[j][e]

            matMul[i][e] = sum

    printMat(matMul, height1, width2)

