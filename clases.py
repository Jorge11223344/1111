from abc import ABC, abstractmethod


class Anuncio(ABC):
    def __init__(self,ancho,alto,url_archivo,url_click,sub_tipo):
        self.__ancho = ancho if ancho > 0 else 1  ## esto es una forma de filtrar en la misma linea, se evita el validador que debería realizarse en otro archivo
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_click = url_click
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self,ancho):
        self.__ancho = ancho

    @property
    def alto(self):
        return self.__alto
    
    @ancho.setter
    def alto(self,alto):
        self.__alto = alto

    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self,url_archivo):
        self.__url_archivo = url_archivo

    @property
    def url_click(self):
        return self.__url_click
    
    @ancho.setter
    def url_click(self,url_click):
        self.__url_click = url_click

    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @ancho.setter
    def sub_tipo(self,sub_tipo):
        self.__sub_tipo = sub_tipo

    @staticmethod
    def mostrar_formatos():
        return {Video.FORMATO} - {Social.FORMATO}
    
    @abstractmethod
    def comprimir_anuncio():
        pass

    @abstractmethod
    def redimensionar_anuncio():
        pass





    


class Campana:
    def __init__(self,nombre,fecha_inicio,fecha_termino):
        anuncios = []
        self.__nombre =nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncio = [self.componer_anuncios()]

    def componer_anuncios(self):

        opcion = int(input("que tipo de anuncio quiere 1-para video 2_para display, 3-para social"))
        if opcion ==1:
            duracion = int(input("cual es la duracion del video minimo 5 minutos"))
            new_anuncio = Video(duracion)
        elif opcion ==2:
            new_anuncio = Display()
        elif opcion ==3:
            new_anuncio = Social()
##  self.__anuncios.append(new_anuncio)
        return new_anuncio

    def agregar_anuncio(self):

        estado = True
        while estado:
            try:
                opcion = int(input("que tipo de anuncio quieres 1 para video 2 para diplay y 3 para social"))
                if opcion ==1:
                    duracion =int(input("cual esla duracion del video minimo es 5 minutos"))
                    new_anuncio = Video(duracion)
                    elif opcion == 2:
                        new_anuncio = Display()
                    elif opcion == 3:
                        new_opcion = Social()
                    elif opcion ==4:
                        estado False
                    self.__anuncios.append(new_anuncio)

                except Exception as e:
                    pass








class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")  ## Parentesis redondo para especificar una tupla

    def __init__(self,duracion):
        self.ancho =1
        self.alto = 1
        self.__duracion = duracion if duracion > 0 else 5

    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self,duracion):
        self.__duracion = duracion

    
    def comprimir_anuncio():
        print("compresion de video no implementado aun")

    
    def redimensionar_anuncio():
        print("recorte de video no implementado")

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")  ## Parentesis redondo para especificar una tupla



    def comprimir_anuncio():
        print("compresion de video no implementado aun")

    
    def redimensionar_anuncio():
        print("recorte de video no implementado")


class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")  ## Parentesis redondo para especificar una tupla



    def comprimir_anuncio():
        print("compresion de video no implementado aun")

    
    def redimensionar_anuncio():
        print("recorte de video no implementado")







