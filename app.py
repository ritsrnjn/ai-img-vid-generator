from flask import Flask, request, jsonify
from onlycalls import create_generic_image, onlycalls_create_character_image
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)


def validate_api_key():
    api_key = request.headers.get('X-API-Key')
    expected_api_key = os.getenv('X-API-Key')

    if not api_key or api_key != expected_api_key:
        return jsonify({"error": "Invalid or missing API key"}), 401

    return None

@app.route('/create-image', methods=['POST'])
def create_image():
    api_key_error = validate_api_key()
    if api_key_error:
        return api_key_error

    data = request.get_json()
    initial_prompt = data.get('initialPrompt')
    if not initial_prompt:
        return jsonify({"error": "initialPrompt is required"}), 400

    image_url = create_generic_image(initial_prompt)
    return jsonify({"url": image_url})


@app.route('/create-character-image', methods=['POST'])
def create_character_image():
    api_key_error = validate_api_key()
    if api_key_error:
        return api_key_error

    data = request.get_json()
    initial_prompt = data.get('initialPrompt')
    character = data.get('character')

    if not character:
        return jsonify({"error": "Please provide the character"}), 400

    character = character.lower()

    # if character not in ["brett", "ponke", "pepe"]: return error
    if character not in ["brett", "ponke", "pepe"]:
        return jsonify({"error": "Invalid character, please choose from [brett, ponke, pepe]"}), 400

    image_url = onlycalls_create_character_image(initial_prompt, character)

    return jsonify({"url": image_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)