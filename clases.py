class Categorias:
    def __init__(self, ids):                     
        self.ids = ids

class Pelicula:                                                                                        
    def __init__(self, id, nombre, fecha, categorias):        
        self.categorias = categorias
        self.id = id                                                                                            
        self.nombre = nombre
        self.fecha = fecha
    
class Persona:
    def __init__(self, id, nombre, nacionalidad):                                 
        self.id = id
        self.nombre = nombre
        self.nacionalidad = nacionalidad


class Plataforma:
    def __init__(self, id, nombre, url):                                        
        self.id = id
        self.nombre = nombre
        self.url = url
class Serie:
    def __init__(self, id, nombre, fecha, categorias):                                                          
        self.id = id
        self.nombre = nombre
        self.fecha = fecha
        self.categorias = categorias 

class Resultados:
    def __init__(self, peliculas = [], series = []):
        self. peliculas = peliculas
        self.series = series    

class Usuario:
    def __init__(self, username, password, coleccion):
        self.username = username
        self.password = password
        self.coleccion = coleccion

class Cine:
    def init(self,nombre,tipo,funciones):
        self.nombre= nombre
        self.tipo= tipo
        self.funciones = funciones