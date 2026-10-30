from .base import Notificacion

class NotificacionEmail(Notificacion):
    def enviar(self, mensaje: str, destinatario: str) -> None:
        print(f"[EMAIL] Enviando a {destinatario}: '{mensaje}'")

class NotificacionSMS(Notificacion):
    def enviar(self, mensaje: str, destinatario: str) -> None:
        print(f"[SMS] Enviando a {destinatario}: '{mensaje}'")

class NotificacionPush(Notificacion):
    def enviar(self, mensaje: str, destinatario: str) -> None:
        print(f"[PUSH] Enviando a {destinatario}: '{mensaje}'")

class NotificacionTelegram(Notificacion):
    def enviar(self, mensaje: str, destinatario: str) -> None:
        print(f"[TELEGRAM] Enviando a {destinatario}: '{mensaje}'")