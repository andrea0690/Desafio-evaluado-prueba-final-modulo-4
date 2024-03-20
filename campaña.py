from datetime import date
from anuncios import campanas


from anuncio import Anuncio, Video, Display, Social
from error import LargoExcedidoException

class Campaña:
    def __init__(self, nombre, anuncios):
        self.__nombre = nombre
        self.__anuncios = []
        self.instanciar_anuncios(anuncios)
        
    def instanciar_anuncios(self, anuncios):
        for a in anuncios:
            tipo = a["tipo"]
            
            if tipo == 'Video':
                for e in a["anuncios"]:
                    self.anuncios.append(Video(e["duracion"]))
            
            if tipo == 'Display':
                for e in a["anuncios"]:
                    self.anuncios.append(Display())
            
            if tipo == 'Social':
                for e in a["anuncios"]:
                    self.anuncios.append(Social())
                
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) <= 50:
            self.__nombre = nuevo_nombre
        else:
            raise LargoExcedidoException("El nombre de la campaña excede maximo", nuevo_nombre, 50)

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio
        
    @property
    def fecha_termino(self):
        return self.__fecha_termino
    
    @fecha_termino.setter
    def fecha_termino(self, fecha_termino):
        self.__fecha_termino = fecha_termino

    @property
    def anuncios(self):
        return self.__anuncios

    def __str__(self):
        anuncios_por_tipo = {}
        for anuncio in self.__anuncios:
            tipo = anuncio.FORMATO
            anuncios_por_tipo[tipo] = anuncios_por_tipo.get(tipo, 0) + 1

        texto = f"Nombre de la campaña: {self.nombre}\n"
        texto += "Anuncios: "
        for tipo, cantidad in anuncios_por_tipo.items():
            texto += f"{cantidad} {tipo}, "

        return texto[:-2]


campana1 = Campaña("verahtfutftutugyukygutfultfutfukjrdyltuftuftufrtyjktfyitfytfytfyitkutfutfyrdkiydrydrykdrydryrdno", campanas)

print(campana1)