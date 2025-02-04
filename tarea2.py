a = float(input("porfavor ingresa un numerito"))
b = float(input("porfavor ingresa un numerito"))
c = float(input("porfavor ingresa un numerito"))
d = float(input("porfavor ingresa un numerito"))
#Determinar el Mayor de los 4 numeritos
if a >= b and a >= c and a >= d:
   mayor = a
elif b >= a and b >= c and b >= d:
   mayor = b
elif c >= a and c >= b and c >= d:
   mayor = c 
else:
   mayor = d 
        
#determinar el menor de los 4 numeritos
if a <= b and a <= c and a <= d:
   menor = a 
elif b <= a and b <= c and b <= d:
    menor = b
elif c <= a and c <= b and c <= d:
    menor = c 
else:
    menor = d 
#imprimir los resultados
print(f"el mayor de los 4 numeritos es: {mayor}")
print(f"el menor de los 4 numeritos es: {menor}")