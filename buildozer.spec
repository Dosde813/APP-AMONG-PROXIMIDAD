[app]
title = AmongUsAudioMod
package.name = amongusvoice
package.domain = org.tu_nombre
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# REQUERIMIENTOS: Aquí incluimos lo que necesita el cel
requirements = python3,kivy,python-socketio,requests,six,websocket-client

# PERMISOS: Muy importante para que funcione el audio y el overlay
android.permissions = INTERNET, RECORD_AUDIO, SYSTEM_ALERT_WINDOW, FOREGROUND_SERVICE

orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a