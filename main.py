import socketio
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
# Necesitamos jnius para hablar con el micrófono de Android directamente
from jnius import autoclass 

sio = socketio.Client()

class ProximityChatApp(App):
    def build(self):
        # SUSTITUYE ESTO POR LA URL QUE TE DE RENDER
        self.url_servidor = "https://tu-app-creada.onrender.com"
        self.room_id = "SALA_GLOBAL" # Aquí pondrán el código de Among Us
        
        layout = BoxLayout(orientation='vertical')
        self.btn = Button(text="CONECTAR Y HABLAR", background_color=(0, 1, 0, 1))
        
        # Al presionar, conecta y activa micro. Al soltar, apaga.
        self.btn.bind(on_press=self.start_comms)
        self.btn.bind(on_release=self.stop_comms)
        
        return layout

    def start_comms(self, instance):
        if not sio.connected:
            sio.connect(self.url_servidor)
            sio.emit('join_room', self.room_id)
        
        self.btn.text = "HABLANDO..."
        self.btn.background_color = (1, 0, 0, 1)
        # Aquí el código envía los paquetes de audio al servidor
        sio.emit('voice_data', {'room': self.room_id, 'audio': '...datos_voz...'})

    def stop_comms(self, instance):
        self.btn.text = "MANTENER PARA HABLAR"
        self.btn.background_color = (0, 1, 0, 1)

if __name__ == '__main__':
    ProximityChatApp().run()