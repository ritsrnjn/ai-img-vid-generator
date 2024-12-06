from flask import Blueprint, request, jsonify
from .service import create_generic_image, create_character_image, create_multi_character_image
import os
from .characters import character_exists, get_list_of_characters

onlycalls_controller = Blueprint('onlycalls_controller', __name__)

def validate_api_key():
    api_key = request.headers.get('X-API-Key')
    expected_api_key = os.getenv('X-API-Key')

    if not api_key or api_key != expected_api_key:
        return jsonify({"error": "Invalid or missing API key"}), 401

    return None


@onlycalls_controller.route('/create-image', methods=['POST'])
def generic_image():
    api_key_error = validate_api_key()
    if api_key_error:
        return api_key_error

    data = request.get_json()
    initial_prompt = data.get('initialPrompt')
    if not initial_prompt:
        return jsonify({"error": "initialPrompt is required"}), 400

    image_url = create_generic_image(initial_prompt)
    return jsonify({"url": image_url})

@onlycalls_controller.route('/create-character-image', methods=['POST'])
def character_image():
    api_key_error = validate_api_key()
    if api_key_error:
        return api_key_error

    data = request.get_json()
    initial_prompt = data.get('initialPrompt')
    character = data.get('character')

    if not character:
        return jsonify({"error": "Please provide the character"}), 400

    character = character.lower()

    if not character_exists(character):
        return jsonify({"error": "Invalid character, please choose from " + get_list_of_characters()}), 400

    image_url = create_character_image(initial_prompt, character)

    return jsonify({"url": image_url})


@onlycalls_controller.route('/create-multi-character-image', methods=['POST'])
def multi_character_image():
    api_key_error = validate_api_key()
    if api_key_error:
        return api_key_error

    data = request.get_json()
    initial_prompt = data.get('initialPrompt')
    character_a = data.get('characterA')
    character_b = data.get('characterB')


    if not character_a or not character_b:
        return jsonify({"error": "Please provide both characters"}), 400

    character_a = character_a.lower()
    character_b = character_b.lower()

    if not character_exists(character_a) or not character_exists(character_b):
        return jsonify({"error": "Invalid character, please choose from " + get_list_of_characters()}), 400

    image_url = create_multi_character_image(initial_prompt, character_a, character_b)

    return jsonify({"url": image_url})

