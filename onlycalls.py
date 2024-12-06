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
    - Adds rich, vivid descriptive elements
    - Chooses a distinctive artistic style (cyberpunk, retro, digital art, etc.)
    - Ensures high visual interest

    Output ONLY the final, enhanced image prompt - no additional text."""

    return generate_text(prompt).strip()


def create_character_image_prompt(initial_prompt, trigger_word):
    prompt = f"""You are an expert image prompt creator. A user has provided this initial prompt: '{initial_prompt}'

    Task: Create a detailed image prompt that:
    - Incorporates the trigger word "{trigger_word}"
    - Describes a scene with the character doing something specific
    - Adds rich narrative and visual details
    - Ensures the trigger word is naturally integrated into the scene

    Output ONLY the final, character-focused image prompt - no additional text."""

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

