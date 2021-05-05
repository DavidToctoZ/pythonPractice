import sys

if(len(sys.argv) == 3):
    num1 = int(sys.argv[1])#FIlas de tabla
    num2 = int(sys.argv[2])#Columnas de tabla
    if((num1 > 0 and num1 <= 9) and (num2 > 0 and num1 <=9)):
        for i in range(0, num1):
            for j in range(0, num2):
                print("*", end="")
            print()
            
    else:
        print("Error, fuera de rango")
        print("Ejemplo: python3 tabla.py 2 5")

else:
    print(len(sys.argv))
    print("Error")
    print("Ejemplo: python3 tabla.py 2 5")
    
