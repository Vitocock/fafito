import requests
import clases

#https://developers.themoviedb.org/3/getting-started/introduction
API_IMAGES = "http://image.tmdb.org/t/p/w500/"
API_KEY = "c4862ec57819cb41b585c3c99130f45b"

def buscarPalabra(query):
  api_url = f"https://api.themoviedb.org/3/search/multi?api_key={API_KEY}&language=en-US&page=1&include_adult=false&query={query}"
  res = requests.get(api_url)

  return res.json()

def buscarDetalles(id, mediaType):
  api_url = f"https://api.themoviedb.org/3/{mediaType}/{id}?api_key={API_KEY}"
  res = requests.get(api_url)

  return res.json()

def crearResultado(resultados):
  series = []
  peliculas = []
  for resultado in resultados:
    if resultado["media_type"] == "tv":
      try:
        nombre = resultado["name"]
      except:
        nombre = resultado["original_name"]
      id = resultado["id"]
      fecha = resultado["first_air_date"] 
      categorias = clases.Categorias(resultado["genre_ids"])
      serie = clases.Serie(id, nombre, fecha, categorias)
      series.append(serie)
    else:
      try:
        nombre = resultado["title"]
      except:
        nombre = resultado["original_title"]
      id = resultado["id"]
      fecha = resultado["release_date"] 
      categorias = clases.Categorias(resultado["genre_ids"])
      pelicula = clases.Pelicula(id, nombre, fecha, categorias)
      peliculas.append(pelicula)
  
  resultadosObj = clases.Resultados(peliculas, series)
  
  return resultadosObj

def mostrarResultados(resultados):
  peliculas = resultados.peliculas
  series = resultados.series

  print("Peliculas: ")
  for pelicula in peliculas:
    print(f"{pelicula.nombre} / {pelicula.fecha} ")
  
  print("Series: ")
  for serie in series:
    print(f"{serie.nombre} / {serie.fecha} ")
  

query = "dragonball" 
resultados = buscarPalabra(query)
resultados = crearResultado(resultados["results"])

mostrarResultados(resultados)
