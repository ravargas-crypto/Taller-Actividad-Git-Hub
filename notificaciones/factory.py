from .base import Notificacion
from .servicios import NotificacionEmail, NotificacionSMS, NotificacionPush, NotificacionTelegram

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
        elif tipo_normalizado == "telegram":
            return NotificacionTelegram()
        else:
            raise ValueError(f"Tipo de notificacion desconocido: '{tipo}'")