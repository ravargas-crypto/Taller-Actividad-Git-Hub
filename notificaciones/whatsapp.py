from .base import Notificacion


class NotificacionWhatsApp(Notificacion):
    def enviar(self, mensaje: str, destinatario: str) -> None:
        print(f"[WHATSAPP] Enviando a {destinatario}: '{mensaje}'")