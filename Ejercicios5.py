
'''Bucles y Funciones
Planteamiento Ejercicios 2
1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci.'''
def Fibonacci(n):
 if(n==0):
  lista = []
  return lista
 elif(n==1):
  lista = [0]
 else:
 
  num1 = 0
  num2 = 1
  lista = [num1,num2]
 
  for i in range(2,n):
   num3 = num1 + num2
   lista.append(num3)
   num1=num2
   num2 =num3
  
 return lista

#print(Fibonacci(10))


'''2. Ejercicio: Define una función que tome un número y retorne una lista de sus
divisores.'''

def divisores(x):
 lista_divisores = [1]
 i = 2
 while i<=x:
  if(x%i==0):
   lista_divisores.append(i)
  i+=1
 return lista_divisores

#print(divisores(7))



'''3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original.'''


def listaUnica(lista):
 listaUnica=[]
 for i in lista:
  if(listaUnica.count(i)==0):
   listaUnica.append(i) 
   
 return listaUnica
num = [1,2,2,2,5,7,5,7,9,9,9,11,11,33,33]
#print(listaUnica(num))


  
 
'''4. Ejercicio: Define una función que tome un número y retorne la suma de sus
dígitos.'''
def sumaDigitos(n):
 while n/10>= 1:
  n = n%10+int(n/10)
 return n

#print('La suma de los digitos es: ',sumaDigitos(87))
 


'''5. Ejercicio: Define una función que tome una cadena y cuente el número de
vocales en la cadena.'''

def cuentaVocales(cadena):
 vocales = ['A','E', 'I', 'O', 'U','a','e','i','o','u']
 count= 0
 for caracter in cadena:
  if vocales.count(caracter)==1:
   count+=1
 return count
cad = 'Amigo'
#print(cuentaVocales(cad))
 

'''6. Ejercicio: Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista.'''
def dev_n_elementos(lista, n):
 i = 0
 while lista[n]>lista[i]:
   print(lista[i])
   i+=1

lista =[1,2,3,4,5,6,7,8]
#dev_n_elementos(lista,5)

'''7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena.'''
def total_may_min(cadena):
 mayusculas = 0
 minusculas = 0
 for c in cadena:
    if c.isupper()== True:
      mayusculas+= 1
    elif c.islower()== True:
      minusculas+= 1
 print('Total de mayusculas:', mayusculas)
 print('Total de minusculas:', minusculas)
cadenas = 'Carlos y Javier son hermanos'
total_may_min(cadenas)


'''8. Ejercicio: Define una función que tome un número y retorne True si es un
número perfecto, False en caso contrario. Un número perfecto es aquel que es
igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.'''

def esNumeroPerfecto(n):
  lista_divisores=divisores(n)
  suma_divisores=0
  for i in lista_divisores:
    suma_divisores= suma_divisores+i
  suma_divisores = suma_divisores-n
  return bool(suma_divisores==n)

#print(esNumeroPerfecto(6))



    


'''9. Ejercicio: Define una función que reciba un número y retorne su
representación en binario.'''
def num_binario(n):
  binario = []
  while n!= 0:
    binario.append(n%2)
    n = int(n/2)
  binario.reverse()
  return binario

print(num_binario(112))



'''10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas).'''
def interseccion_listas(lista1,lista2):
  inter = []
  for i in lista1:
    if(lista2.count(i)!=0):
      inter.append(i)
  return inter
a = [1,3,5,7]
b = [7,5,2]
#print (interseccion_listas(a,b))

'''11. Ejercicio: Define una función que tome una cadena y determine si es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).'''

def esPalindromo(cadena):
  lista = []
  for i in cadena:
    lista.append(i)
  print (lista)
  print(lista.reverse())
  cad2=lista.reverse()
  s =''.join(cad2)
  print(bool(cadena==s))


pal = 'cac'
#esPalindromo(pal) 


'''12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para
múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de
cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco
imprima “FizzBuzz”.'''

def fizz_buzz():
  for i in range(1,51):
    if (int(i%3)==0 and int(i%5)==0):
      print('FizzBuzz')
    elif(i%3==0):
      print('Fizz')
    elif(i%5==0):
      print('Buzz')
    else:
      print(i)

#fizz_buzz() 




'''13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en
orden ascendente.'''
def lista_ordenada(a):
  listaord = sorted(a)

  return listaord

lista_desordenada = [3,17,7,9,2]

#print(lista_ordenada(lista_desordenada))




'''14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y
retorne la lista de palabras que son más largas que n.'''
def pal_mas_largas_que_n(a,n):
  lista_final = []
  for palabra in a:
    if(len(palabra)>n):
      lista_final.append(palabra)
    
  return lista_final
palabras = ['Carlos','Pepe', 'Maria','Aurelio','Jim']
#print (pal_mas_largas_que_n(palabras,4))



'''Planteamiento Ejercicios 3
15. Ejercicio: Define una función que tome un número y calcule su serie de
Fibonacci.'''

#def serieFibonacci(n):

'''16. Ejercicio: Define una función que tome una lista de números y retorne el
número más grande de la lista.'''

def delvuelve_max (a):
  maximo = 0
  for num in a:
    if(num>maximo):
      maximo = num
  return maximo

numeros = [1,7,3,33,19]
print (delvuelve_max(numeros))


'''17. Ejercicio: Define una función que reciba un número y retorne la suma de sus
dígitos al cubo.'''
def suma_digitos_al_cubo(n):
  x=sumaDigitos(n)
  x = x*x*x
  return x

'''18. Ejercicio: Define una función que reciba una lista de números y retorne el
segundo número más grande de la lista.'''
def seg_numero_mas_grande(a):
  x = delvuelve_max(a)
  b = a.remove(x)
  sol = delvuelve_max(b)
  return sol
numeros2 = [9,15,22,45]


#print(seg_numero_mas_grande(numeros2))
  


'''19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al
menos un miembro en común, de lo contrario, retorne False.'''
def un_numero_comun(a,b):
  for miembro in a:
    if(b.count(miembro)>0):
      return bool(True)
    else:
      return bool(False)
print(un_numero_comun(numeros,numeros2))



'''20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos de la lista original en orden inverso.'''

def lista_inversa(a):
  b = a.reverse()
  return b


'''21. Ejercicio: Define una función que reciba una cadena y cuente el número de
dígitos y letras que contiene.'''

def cuenta_letras_y_numeros(cadena):
  
  numeros = 0
  letras = 0
  for elem in cadena:
    if (elem.isnumeric()):
      numeros +=1
    elif(elem.isalpha()):
      letras +=1
  print('Hay',numeros,'numeros y', letras, 'letras' )
texto2 = 'Carlos 18' 
cuenta_letras_y_numeros(texto2)


'''22. Ejercicio: Define una función que reciba una lista de números y retorne la
suma acumulada de los números'''
def suma_lista_de_numeros(lista):
  suma_total = 0
  for num in lista:
    suma_total= suma_total+num
  return suma_total

'''23. Ejercicio: Define una función que encuentre el elemento más común en una
lista.'''
def numero_mas_comun(lista):
  mas_comun = lista[0]
  for elem in lista:
    if(lista.count(elem)>lista.count(mas_comun)):
      mas_comun = elem
  return mas_comun


'''24. Ejercicio: Define una función que tome un número y retorne un diccionario con
la tabla de multiplicar de ese número del 1 al 10.'''
def diccionario_tabla_multiplicar(n):
  tabla_n = {'n*1': n*1, 'n*2': n*2}
  return tabla_n

#print(diccionario_tabla_multiplicar(2))

'''25. Ejercicio: Define una función que tome una cadena y retorne un diccionario
con la cantidad de apariciones de cada caracter en la cadena.'''
def diccionario_cadena(cadena):
  diccionario = {}
  
  for elem in cadena:
    
    diccionario[elem]= cadena.count(elem)
    
  return diccionario

p = 'carrera'
print(diccionario_cadena(p))

'''26. Ejercicio: Define una función que tome dos listas y retorne la lista de
elementos que no están en ambas listas.'''

def elem_distintos(a,b):
  lista_final =[]
  for elem in a:
    if(b.count(elem)==0):
      lista_final.append(elem)
  for elem2 in b :
    if(a.count(elem2)==0):
      lista_final.append(elem2)
  return lista_final

lis_a = [1,3,5,7,8]
lis_b = [2,3,5,9,11]
#print(elem_distintos(lis_a,lis_b))

'''27. Ejercicio: Define una función que tome una lista y retorne la lista sin
duplicados.'''
def elimina_duplicados(a):
  for elem in a:
    if(a.count(elem)>1):
      a.remove(elem)
  return a
lis_c = [1,1,5,7,9,9,7]
print(elimina_duplicados(lis_c))

'''28. Ejercicio: Define una función que reciba un número entero positivo y retorne la
suma de los cuadrados de todos los números pares menores o iguales a ese
número.'''
def suma_cuadrados_pares_menores_n(n):
  suma = 0
  for i in range(0,n+1):
    if(i%2==0):
      suma = suma+(i*i)
  return suma

#print(suma_cuadrados_pares_menores_n(6))


'''29. Ejercicio: Define una función que reciba una lista de números y retorne el
promedio de los números en la lista.'''

def promedio(a):
  promedios = []
  for elem in a:
    promedios.append((a.count(elem)/len(a))*100)
  return promedios
numeros3 = [2,5,6,2,5,5,5]
#print(promedio(numeros3))

'''Planteamiento Ejercicios 4
30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la
cadena más larga en la lista.'''
def cadena_mas_larga(a):
  maximo = a[0]
  for elem in a:
    if(len(elem)>len(maximo)):
      maximo = elem
  return maximo
nombres = ['Carlo', 'Javier', 'Pedro','Nacho']
#print(cadena_mas_larga(nombres))


'''31. Ejercicio: Define una función que reciba un número entero n y retorne una lista
con los n primeros números primos.'''

#lo hago despues del ejercicio 35




'''32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso.'''

def palabras_orden_inverso(cadena):
  inversa=[]
  inversa_cadena=[]
  inversa= cadena.split()
  for i in inversa[::-1]:
    inversa_cadena.append(i)
  cadena_inversa= ' '.join(inversa_cadena)
  print(cadena_inversa)

texto = 'Hola carlos'
#palabras_orden_inverso(texto)

'''33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla.'''
def ordenar_por_ultimo_elemento(lista):
    return sorted(lista, key=lambda x: x[-1])

lista_tuplas = [(1, 5), (3, 2), (7, 8), (4, 1)]
lista_ordenada = ordenar_por_ultimo_elemento(lista_tuplas)
#print(lista_ordenada)





'''34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de
letras vocales en la cadena.'''

#Es igual que el ejercicio 5
#cad = 'hola'
#print(cuentaVocales(cad))


'''35. Ejercicio: Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False.'''
def esPrimo(a):
    i=2
    x = True
    y = False
    while i<=a:
        if(a%i==0):
            if(i!=a):
                print('El numero', a, 'no es primo')
                return y
                break
                
            else:
                print('El numero', a, 'es primo')
                return x
                break
        else :
            i+=1
#print(esPrimo(37))

#ejercicio 31
def lista_numeros_primos(n):
  nprimos=[1]
  i = 1
  while len(nprimos)<n:
      if(esPrimo(i)==True):
        nprimos.append(i)
      i+=1
  return nprimos

#print(lista_numeros_primos(5))



