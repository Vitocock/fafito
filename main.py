import os

from usuarios import *
from funciones import *
from scrapping import *

                                      #######   REGISTRO E INICIO DE SESION   #######

print("Iniciar Sesion [1]\nRegistrarse [2]")

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

os.system("cls")
estrenos = clases.Resultados()
resultados = clases.Resultados()
while True:
  print(f'\nHola, {username}. Que deseas hacer?')
  print("""
  Buscar una pelicula y/o serie [1]
  Ver estrenos [2]
  Ver favoritos [3]
  Guardar en favoritos [4]
  Ver estadisticas [5]
  Salir [0]
  """)
  opcion = int(input("--> "))
  
  os.system("cls")
  if opcion == 1:
    busqueda = str(input("Buscar: "))
    print(f'Buscando "{busqueda}"...')
    resultados = buscarPalabra(busqueda)["results"]
    resultados = crearResultado(resultados)  
    
    mostrarResultados(resultados)
        
  elif opcion == 2:
    print("Cargando estrenos...")
    estrenos = getEstrenos()
    os.system("cls")

    print("ESTRENOS: ")
    mostrarResultados(estrenos)
  
  elif opcion == 3:
    print("Mis Favoritos: ")
    favoritos = getFavoritos(username)
    for favorito in favoritos:
      id = favorito["id"]
      mediaType = favorito["mediaType"]

      detalles = buscarDetalles(id, mediaType)
      mostrarDetalles(detalles, mediaType)
      buscarPlataforma(id, mediaType)

  elif opcion == 4:
    id = int(input("Ingrese la id del contenido: "))
    guardado = False
    
    try:
      if not guardado:
        for estreno in estrenos.peliculas:
          if estreno.id == id:
            print(estreno.nombre)
            guardado = agregarAColeccion(estreno, username)
            break

      if not guardado:
        for resultado in resultados.peliculas:
          if resultado.id == id:
            guardado = agregarAColeccion(resultado, username)
            break
      
      if not guardado:
        for resultado in resultados.series:
          if resultado.id == id:
            guardado = agregarAColeccion(resultado, username)
      
      if not guardado: 
        print("Ha ocurrido un error. Intente realizar una busqueda antes de agregar algo a la su coleccion...")

    except:
        print("Ha ocurrido un error. Intente realizar una busqueda antes de agregar algo a la su coleccion...")    
  
  elif opcion == 5:
    verEstadisticas()
    graficoPlat()


  elif opcion == 0:
    break
    
