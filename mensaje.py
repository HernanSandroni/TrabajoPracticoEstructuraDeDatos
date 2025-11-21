class Mensaje:
    def __init__(self, remitente, destinatario, asunto, cuerpo, urgente=False):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.cuerpo = cuerpo
        self.urgente = urgente

    def __str__(self):
        urg = " (URGENTE)" if self.urgente else ""
        return f"[{self.asunto}{urg}] de {self.remitente} -> {self.destinatario}"
