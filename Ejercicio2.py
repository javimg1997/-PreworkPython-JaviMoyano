#Condicionales
#1. Ejercicio: Dado un número, imprime si es positivo o negativo.
x = -58
if(x<0):
    print('El número es negativo')
else:
    print('El número es positivo')
#2. Ejercicio: Dado un número, imprime si es par o impar.
if(x%2!=0):
    print('El número es impar')
else:
    print ('El número es par')
#3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
x = 17
y = 11
z = 33
if (x>y):
    if(x>z):
        print('Como que', x ,'?')
    else:
        print('Como que',z,'?')
else:
    if(y>z):
        print('Como que',y,'?')
    else:
        print('Como que',z,'?')
    
