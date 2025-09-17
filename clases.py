from datetime import datetime
from typing import List

class Usuario:
    def __init__(self, nombre: str, email: str):
        self.__nombre = nombre
        self.__email = email
        self.__carpetas: List['Carpeta'] = []

    # Getters y setters con propiedades
    @property
    def nombre(self):
        return self.__nombre

    @property
    def email(self):
        return self.__email

    @property
    def carpetas(self):
        return self.__carpetas

    def agregar_carpeta(self, carpeta: 'Carpeta'):
        self.__carpetas.append(carpeta)


class Mensaje:
    def __init__(self, remitente: str, destinatario: str, asunto: str, cuerpo: str, urgente=False):
        self.__remitente = remitente
        self.__destinatario = destinatario
        self.__asunto = asunto
        self.__cuerpo = cuerpo
        self.__fecha = datetime.now()
        self.__urgente = urgente

    @property
    def remitente(self):
        return self.__remitente

    @property
    def destinatario(self):
        return self.__destinatario

    @property
    def asunto(self):
        return self.__asunto

    @property
    def cuerpo(self):
        return self.__cuerpo

    @property
    def fecha(self):
        return self.__fecha

    @property
    def urgente(self):
        return self.__urgente


class Carpeta:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__mensajes: List[Mensaje] = []
        self.__subcarpetas: List['Carpeta'] = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def mensajes(self):
        return self.__mensajes

    @property
    def subcarpetas(self):
        return self.__subcarpetas

    def agregar_mensaje(self, mensaje: Mensaje):
        self.__mensajes.append(mensaje)

    def agregar_subcarpeta(self, carpeta: 'Carpeta'):
        self.__subcarpetas.append(carpeta)


class ServidorCorreo:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__usuarios: List[Usuario] = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def usuarios(self):
        return self.__usuarios

    def registrar_usuario(self, usuario: Usuario):
        self.__usuarios.append(usuario)

    def enviar_mensaje(self, remitente: Usuario, destinatario: str, mensaje: Mensaje):
        for usuario in self.__usuarios:
            if usuario.email == destinatario:
                # Buscar carpeta "Bandeja de Entrada"
                for carpeta in usuario.carpetas:
                    if carpeta.nombre.lower() == "bandeja de entrada":
                        carpeta.agregar_mensaje(mensaje)
                        return True
        return False
