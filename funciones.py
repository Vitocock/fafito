import requests
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

def formatearContenido(contenido): 
  print("HOla")