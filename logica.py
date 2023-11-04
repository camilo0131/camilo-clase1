# number = 5

# print('El valor de la variable es:', number)

# base = int(input('ingrese la base'))
# altura = int(input('ingrese altura'))

# resultado = base * altura

# print('el area del cuadrado es:' , resultado)

#----------------------------------------------------------------

#ejercicio numero (2)

# edad = int(input('ingrese su edad'))

# if edad < 18:
#     print ('eres menor de edad')
# elif edad  >= 18 and  edad <= 65: 
#     print('eres un adulto')
# else :
#     print('eres un adulto mayor')

# #----------------------------------------------------------------


# #ejercicio numero(3)

# edad = int(input('ingrese edad'))
# precio = float(input('ingrese el prtecio del producto'))

# if edad < 18 :
#     print('valor del producto' + str( precio * .90) )
# elif edad >= 65 : 
#     print('valor del producto' + str(precio * .85))
# else :
#     print('el costo de su producto es' + str(precio))    

# #----------------------------------------------------------------


# #ejercicio numero(4)

# puntuacion = int(input('ingrese puntuacion'))

# if puntuacion >=90 :
#     print('sobresaliente')
# elif puntuacion >= 80 and puntuacion <= 89 :
#     print('bueno')
# elif puntuacion >=70 and puntuacion <=79 :
#     print('satisfecho')
# elif puntuacion >= 60 and puntuacion <=69 :
#     print('necesita mejorar')
# else :
#     print('reprobado')

# #---------------------------------------------------------------


# #ejercicio numero (5)
    
    
# salario = float(input('ingrese su salario anual'))

# if salario <= 10000 :
#     print('no se aplica impuesto')
# elif  salario > 10000  and salario <= 50000 :
#     print('debe pagar 10 % de impuesto ' + str(salario * .1))
# elif salario > 50000  and  salario <= 100000 :
#     print('debe pagar 20 % de impuesto' + str(salario * .2))    
# else :
#     print('debe pagar 30% de impuesto' + str(salario * .3))    
    
    
#------------------------------------------------------------------


#bucles

#ejercicio numero (1)

# acendente= 0
# decendente = 11

# while acendente < 10:
#     acendente += 1
#     decendente -= 1
#     print(acendente, '/' , decendente)
    
    
#ejercicio numero (2

# import random

# aleatoreo = random.randint (1, 100)
# adivina = 0

# while adivina != aleatoreo:
#     if adivina == 0:
#         print('inicia el juego')
#     elif adivina < aleatoreo:
#         print('demasiado bajo')    
#     else:
#         print('demasiado alto')    
#     adivina = int (input('ingresa el numero')) 
# print('has ganado')   
    
    
    