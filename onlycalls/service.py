from gpt_service import generate_text
from fal_service import generate_image, generate_image_with_lora, generate_image_with_multiple_loras
from .characters import get_character_config


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


def create_multi_character_image_prompt(initial_prompt, trigger_word_a, trigger_word_b):
    prompt = f"""You are an expert image prompt creator. A user has provided this initial prompt: '{initial_prompt}'

    Task: Create a detailed image prompt that:
    - Incorporates both the characters "{trigger_word_a}" and "{trigger_word_b}", the image should be about these 2 characters specifically
    - Describes a scene with the characters doing something specific
    - Adds rich narrative and visual details
    - Chooses a distinctive artistic style (cyberpunk, retro, digital art, etc.)

    Output ONLY the final, character-focused image prompt - no additional text.

    Here is an example prompt:
    "In a vibrant cyberpunk world bathed in the glow of neon lights, Ponke_meme and Brett_memecoin take center stage, a dynamic duo in the midst of their whimsical ascent. Ponke_meme, with oversized polygonal glasses and a cheeky grin, is captured mid-leap, defying gravity, as his signature triangular antenna stretches triumphantly skyward. Beside him, Brett_memecoin, a sleek figure sporting a futuristic holographic visor and a mischievous smirk, hovers effortlessly, arms outstretched like a digital sorcerer."
"""
    return generate_text(prompt).strip()








def create_generic_image(initial_prompt):
    """Generate a standard image from an initial prompt."""
    final_image_prompt = create_generic_image_prompt(initial_prompt)
    print(final_image_prompt)
    return generate_image(final_image_prompt)

def create_character_image(initial_prompt, character):
    config = get_character_config(character)
    if not config:
        raise ValueError(f"Unsupported character: {character}")

    final_image_prompt = create_character_image_prompt(initial_prompt, config['trigger_word'])
    print(final_image_prompt)
    return generate_image_with_lora(final_image_prompt, config['lora_path'])


def create_multi_character_image(initial_prompt, character_a, character_b):
    config_a = get_character_config(character_a)
    config_b = get_character_config(character_b)


    final_image_prompt = create_multi_character_image_prompt(initial_prompt, config_a['trigger_word'], config_b['trigger_word'])
    print(final_image_prompt)
    return generate_image_with_multiple_loras(final_image_prompt, config_a['lora_path'], config_b['lora_path'])

