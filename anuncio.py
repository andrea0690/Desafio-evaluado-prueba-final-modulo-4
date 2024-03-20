from abc import ABC, abstractmethod

from error import SubTipoInvalidoException

class Anuncio(ABC):
    
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo
        
    @property
    def ancho(self):
        self.__ancho
        
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho if ancho > 0 else 1
        
    @property
    def alto(self):
        self.__alto
        
    @alto.setter
    def alto(self, alto):
        self.__alto = alto if alto > 0 else 1
    
    @property
    def url_archivo(self):
        self.__url_archivo
        
    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo
        
    @property
    def url_clic(self):
        self.__url_clic
        
    @url_clic.setter
    def url_clic(self, url_clic):
        self.__url_clic = url_clic
        
    @property
    def sub_tipo(self):
        self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self, nuevo_sub_tipo):

        if nuevo_sub_tipo in self.SUB_TIPOS:
            self._sub_tipo = nuevo_sub_tipo
        else:
            raise SubTipoInvalidoException("Subtipo no válido", nuevo_sub_tipo, self.SUB_TIPOS)
    
    def comprimir_anuncio():
        pass
        
    def redimencionar_anuncio():
        pass
        
        
class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    
    def __init__(self, duracion: int, url_archivo: str, url_clic: str):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo=self.SUB_TIPOS[0])
        self.__duracion = duracion if duracion > 0 else 5
        
    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, nueva_duracion):
        self.__duracion = nueva_duracion if nueva_duracion > 0 else 5

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")
    
class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")
    def __init__(self, url_archivo: str, url_clic: str):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo=self.SUB_TIPOS[0])
    
    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")
    
class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")
    def __init__(self,url_archivo: str, url_clic: str):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo=self.SUB_TIPOS[0])
    
    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
    
    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")