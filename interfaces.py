from datetime import datetime
from typing import List, Optional


class Mensaje:
    def __init__(self, remitente: str, destinatario: str, asunto: str, cuerpo: str, urgente=False):
        self.__remitente = remitente
        self.__destinatario = destinatario
        self.__asunto = asunto
        self.__cuerpo = cuerpo
        self.__fecha = datetime.now()
        self.__urgente = urgente

    # Propiedades de solo lectura
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
        return list(self.__mensajes)  # devuelve copia

    @property
    def subcarpetas(self):
        return list(self.__subcarpetas)

    def agregar_mensaje(self, mensaje: Mensaje):
        self.__mensajes.append(mensaje)

    def listar_mensajes(self) -> List[str]:
        return [f"{m.fecha} | {m.remitente} -> {m.asunto}" for m in self.__mensajes]

    def agregar_subcarpeta(self, carpeta: 'Carpeta'):
        self.__subcarpetas.append(carpeta)


class Usuario:
    def __init__(self, nombre: str, email: str):
        self.__nombre = nombre
        self.__email = email
        self.__carpetas: List[Carpeta] = []

        # Por defecto cada usuario tiene una bandeja de entrada
        self.agregar_carpeta(Carpeta("Bandeja de Entrada"))

    @property
    def nombre(self):
        return self.__nombre

    @property
    def email(self):
        return self.__email

    @property
    def carpetas(self):
        return list(self.__carpetas)

    def agregar_carpeta(self, carpeta: Carpeta):
        self.__carpetas.append(carpeta)

    def obtener_carpeta(self, nombre: str) -> Optional[Carpeta]:
        for carpeta in self.__carpetas:
            if carpeta.nombre.lower() == nombre.lower():
                return carpeta
        return None

    # Interfaz para enviar mensajes
    def enviar_mensaje(self, servidor: 'ServidorCorreo', destinatario: str, asunto: str, cuerpo: str, urgente=False):
        mensaje = Mensaje(self.__email, destinatario, asunto, cuerpo, urgente)
        return servidor.enviar_mensaje(mensaje)

    # Interfaz para recibir mensajes
    def recibir_mensaje(self, mensaje: Mensaje):
        bandeja = self.obtener_carpeta("Bandeja de Entrada")
        if bandeja:
            bandeja.agregar_mensaje(mensaje)

    # Interfaz para listar mensajes
    def listar_mensajes(self, carpeta_nombre="Bandeja de Entrada"):
        carpeta = self.obtener_carpeta(carpeta_nombre)
        return carpeta.listar_mensajes() if carpeta else []


class ServidorCorreo:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__usuarios: List[Usuario] = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def usuarios(self):
        return list(self.__usuarios)

    def registrar_usuario(self, usuario: Usuario):
        self.__usuarios.append(usuario)

    # Enviar mensaje entre usuarios
    def enviar_mensaje(self, mensaje: Mensaje) -> bool:
        for usuario in self.__usuarios:
            if usuario.email == mensaje.destinatario:
                usuario.recibir_mensaje(mensaje)
                return True
        return False
