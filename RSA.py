# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:01:47 2021

@author: Alejandra Velasco Zárate A01635453 

Este programa cifra mensajes de texto cortos para después encriptarlos con el 
algoritmo RSA y asimismo descenriptarlos y descifrarlos. 

AVISO IMPORTANTE: SI SE DESEA UTILIZAR "TODAS" LAS FUNCIONES NUEVAMENTE PARA CIFRAR, 
ENCRIPTAR, DESENCRIPTAR Y DESCIFRAR, ES IMPORTANTE CORRER EL PROGRAMA DE NUEVO, HACIENDO
CLICK EN 'EJECUTAR ARCHIVO' U OPRIMIENDO LA TECLA 'F5'

Fuciones:

1. key_alphabet:
    esta función te regresa la clave del valor que estás buscando.
    Datos de entrada:
        val: es el valor númerico de la letra que buscas.
    Datos de salida:
        key: es la letra correspondiente. 

2. cifrar:
    esta función separa el mensaje por bloques de dos letras y lo cifra.
    Datos de entrada:
        m: es el mensaje original que desea encriptar.
    Datos de salida: 
        c: es el mensaje cifrado.
    INSTRUCCIONES:
        En la terminal de python, asigne a la variable m el mensaje que quiere 
        cifrar para después encriptar. Por ejemplo:
            m = "hola mundo"
        Después, en la terminal de python escriba la funcion y entre parentesis 
        la variable m 'cifrar(m)'
        
3. rsa_enc:
    esta función encripta el mensaje que fue cifrado anteriormente, con el algoritmo rsa.
    Datos de entrada: 
        c: es el mensaje cifrado anteriormente. 
    Datos de salida:
        ec: es el mensaje encriptado con el algoritmo rsa. 
    INSTRUCCIONES: 
        Esta función solo funciona cuando el mensaje ya esta cifrado. Al utilizar 
        la función cifrar, su mensaje "m" ya esta cifrado y ya se le asignó directamente
        a la variable "c" (que es la entrada de la función 'rsa_enc'). 
        Para encriptar el mensaje "c", en la consola de python escriba rsa_enc(c,n,e), 
        donde (n,e) es la clave pública del receptor y c ya tiene su valor. 
        Si no corrió la función cifrar, es necesario escribir en la terminal 
        de python el valor para 'c'. Por ejemplo: 
            c = [231, 325, 13, 581, 123]
            n = 943
            e = 101
        Con esos valores la función se escribe de la siguiente forma en la consola 
        de python: rsa_enc(c,943,101). Así el resultado será una lista de numeros, 'ec'.
        
4. rsa_des:
    esta función desencripta el mensaje ecnriptado con el algoritmo rsa. 
    Datos de entrada: 
        ec: es el mensaje encriptado. 
    Datos de salida:
        c: es el mensaje ya desencriptado pero todavía cifrado. 
    INSTRUCCIONES:
        Primero se necesita tener el mensaje encriptado, que equivale a la variable
        'ec'. Cuando se corre la función rsa_enc, la varibale 'ec' se le asigna el valor
        de manera automática. Si no se corrió esa función, en la terminal de python, 
        debe asignar a la variable "ec" el mensaje que le enviaron en forma de lista.
        Por ejemplo:
            ec = [507, 331, 192, 772, 41]
        Ya que el valor del mensaje encriptado esta definido, utilizando su clave
        privada (n, d), corre la funcion escribiendo primero el nombre de la función,
        luego el valor de 'n' y luego el valor de 'd' (si (n, d) es (943, 61)):
            rsa_des(ec, 943, 61)
        La salida de la función, será su mensaje desencriptado pero todavía cifrado.
        El mensaje de salida es asignado directamente a la varible 'c'.

5. descifrar:
    esta función descifra el mensaje que fue desencriptado.
    Datos de entrada: 
        c: es el mensaje desencriptado pero todavía cifrado. 
    Datos de salida:
        m: es el mensaje desencriptado y descifrado. El mensaje original. 
    INSTRUCCIONES:
        Cuando se desencripta un mensaje con la función rsa_dec, la variable 'c'
        (que es la variable de entrada de esa función), ya esta asignada directamente
        y lo único que se debe hacer es escribir es la terminal de python:
            decifrar(c)
        Si no se utilizó la función rsa_des para encriptar el mensaje, en la 
        terminal de python necesita asignarle a la variable 'c' los valores obtenidos 
        al desencriptar su mensaje, en forma de lista. Por ejemplo:
            c = [231, 325, 13, 581, 123]
        Ya que asignó a la variable 'c' su mensaje, solo debe escribir en la terminal
        de python 'descifrar(c)'. La salida será el mensaje original que el emisor
        envió desde el principio. 

"""

alphabet = {chr(letter): letter - 64 for letter in range(65, 65 + 26)}
alphabet [" "] = 0

def key_alphabet(val):
    for key, value in alphabet.items():
        if val == value: 
            return key 
        
    return "The key of the value you want does not exist."

a = 0
b = 0
ec = []
m = []
c = []

def cifrar (m):
    c = []
    mensaje_original = list(m.upper())
    if len(mensaje_original) % 2 != 0:
        mensaje_original.append(" ")
    mensaje_original = [mensaje_original[i:i+2] for i in range(0, len(mensaje_original), 2)]
    for i in range(len(mensaje_original)):
         c.append(alphabet[mensaje_original[i][0]] * 27 + alphabet[mensaje_original[i][1]]) 
    return c

def rsa_enc(c, n, e):
    ec = []
    for i in c:
        ec.append(pow(i, e) % n)
        
    return ec

def rsa_des(ec, n, d):
    c = []
    for i in ec:
        c.append(pow(i, d) % n)
        
    return c

def descifrar(c):
    m = []
    for i in c:
        a = i // 27
        b = i % 27
        m.append(key_alphabet(a))
        m.append(key_alphabet(b))
         
    return "".join(m)

#MENU
e = 1
while e != 3:
    e = int(input("Bienvenido al prgrama de encriptación RSA\n\nMENU\n1. Encriptar\n2. Desencriptar\n3. Salir\n\nIngrese la función que desea: "))
    if e == 1:
        m = input("\nIngrese lo que quiera encriptar: ")
        c = cifrar(m)
        n = int(input("Ingrese la clave pública del receptor (n, e):\n\tn: "))
        e = int(input("\te: "))
        ec = rsa_enc(c,n,e)
        print(f"\nEl mensaje encriptado es: {ec}")
    elif e == 2:
        me = input("\nIngrese lo que quiere desencriptar separado por comas sin espacios: ")
        mes = me.split(sep=',')
        ec = list(map(int, mes))
        n = int(input("Ingrese la clave privada (n, d):\n\tn: "))
        d = int(input("\td: "))
        c = rsa_des(ec, n, d)
        m = descifrar(c)
        print(f"\nEl mensaje desencriptado es: {m}")
    elif e == 3: 
        print("\nGracias por usar el programa de encriptación y desencriptación RSA.")
    else: 
        print("\nLa opción que ingresaste no es válida. Favor de ingresar una válida (1,2,3):")

    
    
    