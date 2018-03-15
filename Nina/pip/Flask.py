from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'erro',404

@app.route('/Pave')
def delicias():
    return '<h2>PAVÊ SIMPLES DE CHOCOLATE</h2><br>1 lata de creme de leite <br>1 lata de leite (a mesma medida da lata de creme de leite) <br>2 latas de leite condensado<br> 2 gemas<br>2 colheres de maisena<br>3 colheres de chocolate em pó ou achocolatado<br>biscoito maisena<br>leite para molhar os biscoitos<br>raspas de chocolate (opcional)<br>manteiga sem sal ou margarina, só para dar o ponto'

@app.route('/<name>')
def no(name):
	return"Olá {}".format(name), 200

if __name__ == '__main__':
	app.run()