class Error(Exception):
    pass

class SubTipoInvalidoException(Error):
    
    def __init__(self, mensaje: str, sub_tipo_error: str, sub_tipos: int):
        
        self.mensaje = mensaje
        self.sub_tipo_error = sub_tipo_error
        self.sub_tipos = sub_tipos
        
    def __str__(self) -> str:
        if self.sub_tipo_error == None and self.sub_tipo == None:
            return super().__str__()
        else:
            ret =f"{self.mensaje}."
            if self.sub_tipo_error != None:
                ret += f"Sub tipo ingresado: {self.sub_tipo_error}."
            if self.sub_tipos != None:
                ret += f" Valores permitidos: {''.join(self.sub_tipos)}"
            return ret
        
class LargoExcedidoException(Error):
    
    def __init__(self, mensaje: str, largo: str, maximo: int):
        
        self.mensaje = mensaje
        self.largo = largo
        self.maximo = maximo
        
    def __str__(self) -> str:
        if self.largo == None and self.maximo == None:
            return super().__str__()
        else:
            ret =f"{self.mensaje}."
            if self.largo != None:
                ret += f"texto ingresado: {self.largo}."
            if self.maximo != None:
                ret += f" Máximo {self.maximo} valor permitido."
            return ret