import os

from usuarios import *
from funciones import *

                                      #######   REGISTRO E INICIO DE SESION   #######
print("""
Iniciar Sesion [1]
Registro [2]
""")

opcion = int(input("--> "))
os.system("cls")

if opcion == 1:
  while True:
    print("### INICIO DE SESION ###")
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese su constraseña: ")

    usuario = login(username, password)
    os.system("cls")
    if not usuario:
      print("Nombre de usuario y/o constraseña incorrectos...")
    else:
      print(usuario)
      break
else:
  while True:
    print("### REGISTRO ###")
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese su constraseña: ")

    usuario = registrar(username, password)
    
    os.system("cls")
    if not usuario:
      print("Ese usuario ya existe...")
    else:
      break

                              ########    BUSQUEDA    ######### 
os.system("cls")
while True:
  print(f'Hola, {usuario["username"]}. Que deseas hacer?')
  print("""
  Buscar una pelicula y/o serie [1]
  Ver las estrenos [2]
  Salir [0]
  """)
  opcion = int(input("--> "))
  
  os.system("cls")
  if opcion == 1:
    print("")  
