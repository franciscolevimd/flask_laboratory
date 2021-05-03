from flask import Flask, jsonify
from pokemons_data import pokemons


app = Flask(__name__)


@app.route('/ping')
def index():
	return jsonify({"message":"pokemon!"})


@app.route('/pokemons')
def get_pokemons():
	return jsonify({"page":1, "pokemons":pokemons})


@app.route('/pokemons/<string:name>')
def get_pokemon(name):
	result = {}
	for pokemon in pokemons:
		if pokemon.get('name') == name:
			result = pokemon
			return jsonify({"pokemon":pokemon})
	return jsonify({"message":"Pokemon not found"})


if __name__ == '__main__':
	app.run(debug=True)