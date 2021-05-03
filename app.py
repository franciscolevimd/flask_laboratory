from flask import Flask, jsonify
from pokemons_data import pokemons


app = Flask(__name__)


@app.route('/ping')
def index():
	return jsonify({"message":"pokemon!"})


if __name__ == '__main__':
	app.run(debug=True)