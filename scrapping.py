import requests
from bs4 import BeautifulSoup
from funciones import *
import clases

def obtenerPrecios():
  page = requests.get('https://comparaiso.cl/streaming')  #entrega informacion sobre los precios de las plataformas de streaming
  soup = BeautifulSoup(page.text,'html.parser')
  precios_plat = soup.find('table').find('tbody').find_all('tr')

  plat = []
  prec = []
  for precio in precios_plat:
    plat.append(precio.find_all('th')[0].get_text())
    prec.append(precio.find_all('td')[0].get_text())

  return list(zip(plat,prec))

def getFunciones(url):                                               #Se recolecta informacion de las distintas funciones de la pelicula
  page = requests.get(url)                                                   
  soup = BeautifulSoup(page.text,'html.parser')
  funcionesP = soup.find_all(class_="cont-datos")
  cines=[]

  for funciones in funcionesP:
    filas = funciones.find_all('tr')
    for fila in filas:
      nombre = fila.find_all('td')[0].getText().capitalize()
      tipo = fila.find_all('td')[1].getText().capitalize()
      horario = fila.find_all('td')[2].getText().capitalize()
      cine = clases.Cine(nombre,tipo,horario )
      cines.append(cine)
  
  return cines

def getEstrenos():
  page = requests.get('https://decartelera.cl/cartelera')
  soup = BeautifulSoup(page.text,'html.parser')
  listaPeliculas = soup.find_all(class_="col col-sm-4 col-md-3 mb-4")
  peliculas = []

  for resultado in listaPeliculas:
    nombre = resultado.find(class_='card-title').text
    try:
      peliculaRes = buscarPalabra(nombre)["results"][0]
    except:
      continue

    try:
      nombre = peliculaRes["title"]
    except:
      nombre = peliculaRes["original_title"]
      
    id = peliculaRes["id"]
    fecha = peliculaRes["release_date"] 
    categorias = clases.Categorias(peliculaRes["genre_ids"])
    pelicula = clases.Pelicula(id, nombre, fecha, categorias)

    peliculas.append(pelicula)
    
  return clases.Resultados(peliculas, [])

def estrenosFunciones():
  page = requests.get('https://decartelera.cl/cartelera')
  soup = BeautifulSoup(page.text,'html.parser')
  listaPeliculas = soup.find_all(class_="col col-sm-4 col-md-3 mb-4")
  i=1
  for pelicula in listaPeliculas:
    nombre = pelicula.find(class_='card-title').text
    fecha = pelicula.find(class_='card-text text-center text-muted').text
    url = pelicula.find_all('a')[0]["href"]
  
    print(i, " - ", nombre, "(Estrenada el",fecha ,"                             ")
    i+=1
    funciones = getFunciones(url)


