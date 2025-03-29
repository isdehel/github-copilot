#Pide al usuario que introduzca dos números y llama a las funciones creadas anteriormente para hacer las operaciones
a = int(input("Introduce un número: "))
b = int(input("Introduce otro número: "))


#añade una función que sume dos número y devuelva el resultado
def suma(a,b):
    return a + b



#añade una función que reste dos número y devuelva el resultado
def resta(a,b):
    return a - b


#añade una función que multiplique dos número y devuelva el resultado
def multiplicacion(a,b):
    return a * b



#añade una función que divida dos número y devuelva el resultado
def division(a,b):
    return a / b


print("La suma de los números es: ", suma(a,b))
print("La resta de los números es: ", resta(a,b))
print("La multiplicación de los números es: ", multiplicacion(a,b))
print("La división de los números es: ", division(a,b))

