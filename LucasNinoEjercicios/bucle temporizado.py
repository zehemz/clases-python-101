import time
import webbrowser
url = raw_input ("ingrese la url ej: www.google.com \n")
seg = input ("ingrese los segundos de espera \n")
while True:
    print "en espera"
    time.sleep (seg)    
    webbrowser.open_new_tab("http://" + url)
    print "direccionando"
