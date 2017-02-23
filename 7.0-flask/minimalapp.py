from flask import Flask


app = Flask(__name__) #nuestra WSGI application. (web server gateway interfase, es una interfase universal web apps - web servers)
'''
Si es una apicación monomodulo, va '__main__' (que es la variable __name__)
Caso contrario un import name.
Es necesario para que flask ubique: template, statics, etc.
'''

@app.route('/') #app es la clase, route() es un método decorador.
def hello_world():
    return 'Hello, world'
