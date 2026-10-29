from abc import ABC, abstractmethod

class Notificacion(ABC):
    """Interfaz abstracta para los canales de notificación."""

    @abstractmethod
    def enviar(self, mensaje: str, destinatario: str) -> None:
        pass