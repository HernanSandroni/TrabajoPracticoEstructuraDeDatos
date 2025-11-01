# filtros.py
# Aquí definimos filtros automáticos para organizar mensajes según reglas del usuario

from typing import List, Dict

# Cada mensaje será un diccionario con campos básicos
# Ejemplo de mensaje:
# mensaje = {"remitente": "juan@gmail.com", "asunto": "Trabajo", "urgente": True, "carpeta": "inbox"}

def filtrar_por_remitente(mensajes: List[Dict], remitente: str) -> List[Dict]:
    """
    Filtra los mensajes que vienen de un remitente específico.
    """
    return [m for m in mensajes if m["remitente"] == remitente]

def filtrar_por_asunto(mensajes: List[Dict], palabra_clave: str) -> List[Dict]:
    """
    Filtra los mensajes cuyo asunto contiene la palabra clave.
    """
    return [m for m in mensajes if palabra_clave.lower() in m["asunto"].lower()]

def filtrar_urgentes(mensajes: List[Dict]) -> List[Dict]:
    """
    Filtra los mensajes marcados como urgentes.
    """
    return [m for m in mensajes if m.get("urgente", False)]

def mover_a_carpeta(mensajes: List[Dict], nombre_carpeta: str) -> None:
    """
    Mueve los mensajes a la carpeta indicada.
    Modifica los diccionarios de los mensajes directamente.
    """
    for m in mensajes:
        m["carpeta"] = nombre_carpeta

# Ejemplo de uso
if __name__ == "__main__":
    mensajes = [
        {"remitente": "juan@gmail.com", "asunto": "Trabajo", "urgente": True, "carpeta": "inbox"},
        {"remitente": "ana@gmail.com", "asunto": "Fiesta", "urgente": False, "carpeta": "inbox"},
        {"remitente": "juan@gmail.com", "asunto": "Proyecto", "urgente": False, "carpeta": "inbox"}
    ]

    urgentes = filtrar_urgentes(mensajes)
    print("Mensajes urgentes:", urgentes)

    juan_msgs = filtrar_por_remitente(mensajes, "juan@gmail.com")
    print("Mensajes de Juan:", juan_msgs)

    filtrar_por_asunto(mensajes, "proyecto")
    mover_a_carpeta(juan_msgs, "trabajo")
    print("Mensajes después de mover a carpeta:", mensajes)
