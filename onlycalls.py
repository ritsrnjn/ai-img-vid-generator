from gpt_service import generate_text
from fal_service import generate_image, generate_image_with_lora

# Character LoRA configurations
BRETT_LORA_PATH = "https://storage.googleapis.com/fal-flux-lora/bb6ec5438d5c4ca7897cbf0df40fb051_pytorch_lora_weights.safetensors"
PEPE_LORA_PATH = "https://v3.fal.media/files/zebra/Ty7OLVtSbSA7RHor8B-Kp_pytorch_lora_weights.safetensors"
PONKE_LORA_PATH = "https://v3.fal.media/files/tiger/AmoMe4SZjfGXkbe3W0DaP_pytorch_lora_weights.safetensors"

BRETT_TRIGGER_WORD = "Brett_memecoin"
PEPE_TRIGGER_WORD = "PEPE_token"
PONKE_TRIGGER_WORD = "Ponke_meme"

def create_generic_image_prompt(initial_prompt):
    prompt = f"""You are an expert image prompt creator. A user has provided this initial prompt: '{initial_prompt}'

    Task: Generate a highly detailed, creative image prompt that:
    - Expands on the user's initial ideas
    - Adds rich, vivid descriptive elements and keep the images realistic.
    - Use the terms realistic and cyberpunkish or futuristic to describe the image.
    - Always Chooses a distinctive artistic style (cyberpunk, futuristic, modern etc.)
    - Ensures high visual interest

    Output ONLY the final, enhanced image prompt - no additional text.

    Here is an example prompt:
    Cyberpunkish theme, 5 rich people partying on a floating platform on boosters with Newyork background in night"
"""

    return generate_text(prompt).strip()


def create_character_image_prompt(initial_prompt, trigger_word):
    prompt = f"""You are an expert image prompt creator. A user has provided this initial prompt: '{initial_prompt}'

    Task: Create a detailed image prompt that:
    - Incorporates the character "{trigger_word}", the image should be about this character specifically
    - Describes a scene with the character doing something specific
    - Adds rich narrative and visual details
    - Chooses a distinctive artistic style (cyberpunk, retro, digital art, etc.)

    Output ONLY the final, character-focused image prompt - no additional text.
    
    Here is an example prompt:
    "In a vibrant cyberpunk scene illuminated by the glow of neon lights, Ponke_meme, an enigmatic character with oversized polygonal glasses and a cheeky grin, takes center stage. He is depicted mid-leap, as if defying gravity, with his signature triangular antenna extending triumphantly to the sky. Below his feet, the digital representation of a stock market graph soars steeply upward, symbolized by pixelated cryptocurrencies represented as colorful, futuristic coins spinning in orbit around him. The moon looms large and majestic in the background, its surface adorned with glistening, holographic cityscapes. The sky is an electric swirl of purples, blues, and pinks, creating a digital haze that enhances the sense of boundless potential and whimsical adventure. The style brings an amalgamation of retro digital art with a touch of sci-fi aesthetics, capturing the momentum of Ponke_meme's unlikely but unstoppable journey to the moon."

"""

    return generate_text(prompt).strip()


def create_generic_image(initial_prompt):
    """Generate a standard image from an initial prompt."""
    final_image_prompt = create_generic_image_prompt(initial_prompt)
    print(final_image_prompt)
    return generate_image(final_image_prompt)


def onlycalls_create_character_image(initial_prompt, character):
    character_configs = {
        'brett': {
            'lora_path': BRETT_LORA_PATH,
            'trigger_word': BRETT_TRIGGER_WORD
        },
        'pepe': {
            'lora_path': PEPE_LORA_PATH,
            'trigger_word': PEPE_TRIGGER_WORD
        },
        'ponke': {
            'lora_path': PONKE_LORA_PATH,
            'trigger_word': PONKE_TRIGGER_WORD
        }
    }

    config = character_configs.get(character.lower())
    if not config:
        raise ValueError(f"Unsupported character: {character}")

    final_image_prompt = create_character_image_prompt(initial_prompt, config['trigger_word'])
    print(final_image_prompt)
    return generate_image_with_lora(final_image_prompt, config['lora_path'])

