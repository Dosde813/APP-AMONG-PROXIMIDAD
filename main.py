import socketio
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from android.permissions import request_permissions, Permission
import threading

# Configuración del Servidor
URL_RENDER = "https://among-proximidad.onrender.com"
sio = socketio.Client()

class ProximityChatApp(App):
    def build(self):
        # Pedir permisos de micrófono al abrir la app
        request_permissions([Permission.RECORD_AUDIO, Permission.INTERNET])
        
        self.room_id = "SALA1" # Puedes cambiar esto por el código de Among Us
        
        layout = BoxLayout(orientation='vertical', padding=10)
        self.label = Label(text="Estado: Desconectado", size_hint_y=0.2)
        
        self.btn = Button(
            text="CONECTAR Y HABLAR", 
            background_color=(0, 1, 0, 1),
            font_size='20sp'
        )
        
        # Eventos del botón
        self.btn.bind(on_press=self.start_comms)
        self.btn.bind(on_release=self.stop_comms)
        
        layout.add_widget(self.label)
        layout.add_widget(self.btn)
        return layout

    def start_comms(self, instance):
        try:
            if not sio.connected:
                sio.connect(URL_RENDER)
                sio.emit('join_room', self.room_id)
                self.label.text = f"Conectado a: {self.room_id}"
            
            self.btn.text = "¡ESTÁS HABLANDO!"
            self.btn.background_color = (1, 0, 0, 1)
            
            # Aquí le decimos al servidor que estamos enviando audio
            # (En una versión Pro aquí iría el flujo de bytes del micro)
            sio.emit('voice_data', {'room': self.room_id, 'audio': 'mic_on'})
            
        except Exception as e:
            self.label.text = f"Error: {str(e)}"

    def stop_comms(self, instance):
        self.btn.text = "MANTENER PARA HABLAR"
        self.btn.background_color = (0, 1, 0, 1)
        if sio.connected:
            sio.emit('voice_data', {'room': self.room_id, 'audio': 'mic_off'})

# Escuchar cuando otros hablan (para que suene en tu cel)
@sio.on('play_audio')
def on_audio(data):
    print("Recibiendo señal de audio de un amigo...")
    # Aquí es donde el cel de tu amigo activaría el parlante

if __name__ == '__main__':
    ProximityChatApp().run()
