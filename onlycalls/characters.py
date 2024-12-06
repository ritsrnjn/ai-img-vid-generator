# character.py

# Character LoRA configurations
CHARACTER_CONFIGS = {
    'brett': {
        'lora_path': "https://storage.googleapis.com/fal-flux-lora/bb6ec5438d5c4ca7897cbf0df40fb051_pytorch_lora_weights.safetensors",
        'trigger_word': "Brett_memecoin"
    },
    'pepe': {
        'lora_path': "https://v3.fal.media/files/zebra/Ty7OLVtSbSA7RHor8B-Kp_pytorch_lora_weights.safetensors",
        'trigger_word': "PEPE_token"
    },
    'ponke': {
        'lora_path': "https://v3.fal.media/files/tiger/AmoMe4SZjfGXkbe3W0DaP_pytorch_lora_weights.safetensors",
        'trigger_word': "Ponke_meme"
    }
}


def get_character_config(character):
    """
    Retrieve configuration for a specific character.

    Args:
        character (str): Name of the character (case-insensitive)

    Returns:
        dict: Character configuration

    Raises:
        ValueError: If character is not found
    """
    config = CHARACTER_CONFIGS.get(character.lower())
    if not config:
        raise ValueError(f"Unsupported character: {character}")
    return config


# check if the character exists
def character_exists(character):
    return character.lower() in CHARACTER_CONFIGS

def get_list_of_characters():
    # return comma separated list of characters
    return ', '.join(CHARACTER_CONFIGS.keys())