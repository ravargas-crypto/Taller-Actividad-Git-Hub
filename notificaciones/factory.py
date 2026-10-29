from .base import Notificacion
from .servicios import NotificacionEmail, NotificacionSMS, NotificacionPush

class NotificacionFactory:
    @staticmethod
    def crear_notificacion(tipo: str) -> Notificacion:
        tipo_normalizado = tipo.strip().lower()

        if tipo_normalizado == "email":
            return NotificacionEmail()
        elif tipo_normalizado == "sms":
            return NotificacionSMS()
        elif tipo_normalizado == "push":
            return NotificacionPush()
        else:
            raise ValueError(f"Tipo de notificacion desconocido: '{tipo}'")