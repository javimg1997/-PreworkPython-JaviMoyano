#Bucles
#1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for x in nums:
    if(x<=10):
        print(x)

#2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
i = 1
while i<=20:
    if(i%2==0):
        print(i)
    i+=1
    
    


#3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
y=1
total=0
while y<=100:
    total = total+y
    y+=1
print(total)

