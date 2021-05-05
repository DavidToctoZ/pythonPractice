import sys

if(len(sys.argv) == 2):
    num = int(sys.argv[1])
    
    if(num > 0):
        lonNum = len(str(num))
        cont = 0
        for i in range(lonNum -1, -1, -1):
            
            x = (10**cont * int(str(num)[i]))
            print("{:04d}".format(x))     
            cont += 1
    else:
        print("Error")
        print("Ejemplo: python3 descomposicion.py [0 <]")

else:
    print("Error")
    print("Ejemplo: python3 descomposicion.py [0 <]")




