class Categoria:
    def __init__(self, nombreCategoria, id):                     
        self.nombreCategoria = nombreCategoria
        self.id = id

class Pelicula:                                                                                        
    def __init__(self, id, nombrePeli, fechaPeli, categorias):        
        self.categorias = categorias
        self.id = id                                                                                            
        self.nombrePeli = nombrePeli
        self.fechaPeli = fechaPeli
    
class Persona:
    def __init__(self, id, nombreActor,nacionalidadActor):                                 
        self.id = id
        self.nombreActor = nombreActor
        self.nacionalidadActor = nacionalidadActor


class Plataforma:
    def __init__(self, id,nombrePlataforma):                                        
        self.id = id
        self.nombrePlataforma = nombrePlataforma


#Series#
class Serie:
    def __init__(self, id, nombreSerie, fechaSerie):                                                          
        self.nombreSerie = nombreSerie
        self.fechaSerie = fechaSerie

        
#Estrenos#
class Estrenos:
    def __init__(self, peliculas, series):                        
        self.peliculas = peliculas
        self.series = series

class Resultados:
    def __init__(self, resultados):
        self.resultados = resultados

class Usuario:
    def __init__(self, contrasena, username, favoritos):
        self.username = username
        self.contrasena = contrasena
        self.favoritos = favoritos
