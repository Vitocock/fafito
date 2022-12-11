import json
import clases
from funciones import buscarPlataforma

def login(username, password):
  archivo = open("usuarios.json")
  archivoJson = json.load(archivo)
  usuarios = archivoJson["usuarios"]

  for usuario in usuarios: # Verificar que el usuario no existe
    if usuario["username"] == username and usuario["password"] == password:
      archivo.close()
      return usuario
  archivo.close()
  return False

def registrar(username, password):
  archivo = open("usuarios.json")
  archivoJson = json.load(archivo)
  usuarios = archivoJson["usuarios"]

  for usuario in usuarios: # Verificar que el usuario no existe
    if usuario["username"] == username:
      return False
  archivo.close()

  archivo = open("usuarios.json", "w")
  usuario = clases.Usuario(username, password, [], {}) 
  archivoJson["usuarios"].append(usuario.__dict__)
  json.dump(archivoJson, archivo)
  archivo.close()

  return login(username, password)

def agregarAColeccion(contenido, username):
  archivo = open("usuarios.json")
  archivoJson = json.load(archivo)
  archivo.close()
  usuarios = archivoJson["usuarios"]

  archivo = open("usuarios.json", "w")
  for usuario in range(len(usuarios)):
    if usuarios[usuario]["username"] == username:
      if isinstance(contenido, clases.Pelicula):
        mediaType = "movie"
      else: 
        mediaType = "tv"

      plataformas = buscarPlataforma(contenido.id, mediaType) #[PLAT, PLAT]
      platGuardadas = usuarios[usuario]["plataformas"] #{}
      for plataforma in plataformas:
        nombre = plataforma.nombre
        try:
          platGuardadas[nombre] += 1
        except:
          platGuardadas[nombre] = 1
          
      usuarios[usuario]["plataformas"] = platGuardadas
      usuarios[usuario]["coleccion"].append({ "mediaType" : mediaType, "id" : contenido.id })

  archivoJson["usuarios"] = usuarios
  json.dump(archivoJson, archivo)
  archivo.close()

  return True

def getFavoritos(username): 
  archivo = open("usuarios.json")
  archivoJson = json.load(archivo)
  usuarios = archivoJson["usuarios"]

  for usuario in range(len(usuarios)):
    if usuarios[usuario]["username"] == username:
      archivo.close()
      return usuarios[usuario]["coleccion"] 
  
  archivo.close()
  return []
