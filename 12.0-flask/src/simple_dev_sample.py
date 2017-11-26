'''
This module represents the (otherwise anonymous) scope in which the interpreter’s main program executes — commands read either from standard input, from a script file, or from an interactive prompt. It is this environment in which the idiomatic “conditional script” stanza causes a script to run:

Instalación de flask:

$ pip install Flask

Ejecución de flask:
$ python simple_dev_sample.py

Esto nos proveerá de una instancia de programa corriendo y escuchando en el puerto 5000
de manera local
 * Running on http://localhost:5000/
'''
from flask import Flask
app = Flask(__name__)


if __name__ == "__main__":
    #Main script
    print("Running flask example ...")
    #Variable global, ejecuta run.
    app.run()



@app.route("/")
def hello():
    return "Hello World!"
