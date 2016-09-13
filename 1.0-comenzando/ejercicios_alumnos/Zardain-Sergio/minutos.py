import time
import webbrowser

#variable contadorque sirve para mostrar por pantalla cuanto tiempo va transcurriendo.
contador = 0
#URL de un video de musica de youtube
url = "https://www.youtube.com/watch?v=IBH97ma9YiI"
#cantidad de minutos que tienen que transcurrir para que se abra el navegador
minutos = 1
#variable en la que se almacena el tiempo de espera final
timeout = time.time() + 60*minutos

while True:
    #si lavariable mantiene el mismo valor entonces no tiene que volver a ejecutarse esta instrucción
    if contador != int(time.clock()):
        contador = int(time.clock())
        print("Segundo transcurrido: " + str(contador))
    
    #si coincide significa que pasó el tiempo de espera
    if time.time() > timeout:
        webbrowser.open_new(url)
        break  
