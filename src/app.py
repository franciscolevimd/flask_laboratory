from flask import Flask, jsonify, request
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
	pokemon = found_pokemon_by_name(name)
	if pokemon:
		return jsonify({"pokemon":pokemon})
	return jsonify({"message":"Pokemon not found"})


@app.route('/pokemons', methods=['POST'])
def add_pokemon():
	new_pokemon = { 
		'name': request.json['name'], 
		'url': request.json['url']
	}
	pokemons.append(new_pokemon)
	return 	jsonify({'message':'Pokemon added succesfully.', 'pokemons':pokemons})


@app.route('/pokemons/<string:name>', methods=['PUT'])
def update_pokemon(name):
	pokemon = found_pokemon_by_name(name)
	if pokemon:
		pokemon['name'] = request.json['name']
		pokemon['url'] = request.json['url']
		return jsonify({
			'message':'Pokemon updated.',
			'pokemon':pokemon
		})
	return jsonify({'message':'Pokemon not found.'})


@app.route('/pokemons/<string:name>', methods=['DELETE'])
def delete_pokemon(name):
	pokemon = found_pokemon_by_name(name)
	if pokemon:
		pokemons.remove(pokemon)
		return jsonify({
			'message':'Pokemon deleted.',
			'pokemons':pokemons
		})
	return jsonify({'message':'Pokemon not found.'})


def found_pokemon_by_name(name):
	for pokemon in pokemons:
		if pokemon.get('name') == name:
			return pokemon
	return None


if __name__ == '__main__':
	app.run(debug=True)