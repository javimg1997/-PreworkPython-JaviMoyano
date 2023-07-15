#Funciones
#1. Ejercicio: Define una función que tome dos números y retorne su suma.
def suma(a,b):
    res = a+b
    return res
print(suma (2,31))
#2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
def factorial (x):
    res= 1
    while x>0:
        res = res * x
        x-= 1
    return res
print(factorial(4))
#3. Ejercicio: Define una función que tome un número y determine si es primo.
def esPrimo(a):
    i=2
    while i<=a:
        if(a%i==0):
            if(i!=a):
                print('El numero', a, 'no es primo')
                break
                
            else:
                print('El numero', a, 'es primo')
                break
        else :
            i+=1
esPrimo(37)
            
         
#4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
#de ellos.
def sumaLista(a):
 suma = 0
 for numero in a:
      suma += numero
 return suma

miLista = [2,4,6]
print(sumaLista(miLista))
#5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
#cadena en reversa.

def cadenaReversa(cadena):
    cadena_invertida = cadena[::-1]
    return cadena_invertida
print(cadenaReversa('Carlos'))
