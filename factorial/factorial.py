print("---------------------------------------------")
print("-------------NUMERO-FACTORIAL----------------")
print("---------------------------------------------")



#input
def factorial(num):

#Processing
    if num < 0: 
        print("Factorial of negative num does not exist")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

num = int(input()); 

#output 
print("factorial de: ",num,"es", factorial(num))