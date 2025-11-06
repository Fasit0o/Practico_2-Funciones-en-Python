#Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “c”. Llamar a esta función desde el
#programa principal

def imprimir_hola_mundo():
    return "c"

imprimir_hola_mundo()


#Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return (f"Hola {nombre}!")

nom = input("Ingrese su nombre de usuario")
saludar_usuario(nom)


#Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    return (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Inserte su nombre")
apellido = input("Inserte su apellido")
edad = int(input("Inserte su edad"))
residencia = input("Inserte su residencia")

informacion_personal(nombre, apellido, edad, residencia)


#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
#calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
#Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math

def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

radio = float(input("Ingrese el radio del circulo: "))

print(f"El area del circulo es: {calcular_area_circulo(radio):.2f}")
print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio):.2f}")


#Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

seg = int(input("Ingrese la cantidad de segundos: "))
print(f"{seg} segundos equivalen a {segundos_a_horas(seg):.2f} horas.")


#Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11, 1):
        multiplicar = numero * i
        print(f"{numero} x {i} = {multiplicar}")

a = int(input("Ingrese un numero: "))
tabla_multiplicar(a)


#Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
#Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

numero = float(input("Ingrese un numero: "))
numero1 = float(input("Ingrese otro numero: "))

resultado = operaciones_basicas(numero, numero1)

print(f"""
Resultados:
La suma es: {resultado[0]}
La resta es: {resultado[1]}
La multiplicacion es: {resultado[2]}
La division es: {resultado[3]}
""")


#Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

resultado = calcular_imc(peso, altura)

print(f"Su índice de masa corporal (IMC) es: {resultado:.2f}")


#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp = float(input("Ingrese la temperatura en grados Celsius: "))

resultado = celsius_a_fahrenheit(temp)

print(f"La temperatura en Fahrenheit es: {resultado:.2f}")


#Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

print(f"El promedio entre {num1}, {num2} y {num3} es: {calcular_promedio(num1, num2, num3):.2f}")
