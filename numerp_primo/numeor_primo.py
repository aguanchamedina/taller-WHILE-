#input
n = int(input("Digite el numero: "))

#processing 
def evaluar_primo(n):
    contador = 0 
    resultado = True 
    for i in range(1, n+1):
        if (n%1==0):
            contador+=1
        if (contador>2):
            resultado= False 
            break 
    return resultado 

#output 
if (evaluar_primo(n) == True):
    print("El numero es primo")
else :
    print("El numero no es primo")   