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

def mostrarDetalles(detalles, mediaType):
  if mediaType == "movie":
    try:
      nombre = detalles["title"]
    except:
      nombre = detalles["original_title"]
    sinopsis = detalles["overview"]
    fecha = detalles["release_date"] 
    print(f"\n\t\t\t{nombre} | {fecha}\n{sinopsis}\n")

  else:
    try:
      nombre = detalles["name"]
    except:
      nombre = detalles["original_name"]
    sinopsis = detalles["overview"]
    fecha = detalles["first_air_date"] 
    print(f"\n\t\t\t{nombre} | {fecha}\n{sinopsis}\n")

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
  i = False
  
  if len(peliculas):
    i = True
    print("\nPeliculas: ")
    for pelicula in peliculas:
      print(f"\t{pelicula.nombre} / {pelicula.fecha} / [{pelicula.id}] ")

      
  if len(series):   
    i = True
    print("\nSeries: ")
    for serie in series:
      print(f"\t{serie.nombre} / {serie.fecha} / [{serie.id}]")
  
  if not i:
    print("No se han encontrado resultados...")

def getId2(id,mediatype,):         #obtiene id de imbd para utilizarlo con la segunda api
  api_url = f"https://api.themoviedb.org/3/{mediatype}/{id}/external_ids?api_key={API_KEY}&language=en-US"
  res = requests.get(api_url)

  return res.json()

def PlataformaRes(id):    #entrega de un json por parte de la api
    url = f"https://watchmode.p.rapidapi.com/title/{id}/sources/"

    headers = {
        "regions": "US",
        "X-RapidAPI-Key": "5645de1cdfmsh6f1599cb7c8d9a8p16d7d0jsne1f4c90a392e",
        "X-RapidAPI-Host": "watchmode.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    return response.json()

def Plataforma(id):             #entrega la lista de plataformas junto a la url 
    res = PlataformaRes(id)

    NPlat = []
    for res in res:
        nombre = res["name"]
        id2 = res["source_id"]
        url = res["web_url"]
        Plataforma = clases.Plataforma(id2,nombre,url)
        NPlat.append(Plataforma)

    url = ""
    for Plataforma in NPlat:
      if Plataforma.url != url:
        print(f"{Plataforma.nombre},{Plataforma.url}")
      url = Plataforma.url
        
def buscarPlataforma(id, mediatype):  #busca la plataforma
    res2 = getId2(id, mediatype)

    Plataforma(res2['imdb_id'])