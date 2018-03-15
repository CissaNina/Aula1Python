rom flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/Pave')
def pave():
    return 'PAVÊ SIMPLES DE CHOCOLATE'
   	return '1 lata de creme de leite' + '1 lata de leite (a mesma medida da lata de creme de leite)' +
   	'2 latas de leite condensado' + '2 gemas'
