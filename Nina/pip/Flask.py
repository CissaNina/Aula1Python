from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/Rotas')
def Rotas():
    return 'Meu'

if __name__ =='__main__':
	app.run()