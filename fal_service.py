import fal_client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
           print(log["message"])


def generate_image(prompt):
    try:
        result = fal_client.subscribe(
            "fal-ai/flux-pro/v1.1-ultra",
            arguments={
                "prompt": prompt,
            },
            with_logs=True,
            on_queue_update=on_queue_update,
        )

        if result and result.get('images') and len(result['images']) > 0:
            return result['images'][0]['url']
        else:
            print("No image URL found in the response")
            return "ERROR"
    except Exception as e:
        print(f"Error generating image: {str(e)}")
        return "ERROR"


def generate_image_with_lora(prompt, lora_path):

    try:
        # Make the API call with Lora configuration
        result = fal_client.subscribe(
            "fal-ai/flux-lora",
            arguments={
                "prompt": prompt,
                "loras": [
                    {
                        "path": lora_path,
                        "scale": 1
                    }
                ],
                "embeddings": [],
                "image_size": "portrait_16_9",
                "num_inference_steps": 28,
                "guidance_scale": 3.5,
                "enable_safety_checker": True
            }
        )

        # Extract the image URL from the result
        if result and result.get('images') and len(result['images']) > 0:
            return result['images'][0]['url']
        else:
            return "No image URL found in the response"

    except Exception as e:
        return f"Error generating image: {str(e)}"




# Character LoRA configurations
BRETT_LORA_PATH = "https://storage.googleapis.com/fal-flux-lora/bb6ec5438d5c4ca7897cbf0df40fb051_pytorch_lora_weights.safetensors"
PEPE_LORA_PATH = "https://v3.fal.media/files/zebra/Ty7OLVtSbSA7RHor8B-Kp_pytorch_lora_weights.safetensors"
PONKE_LORA_PATH = "https://v3.fal.media/files/tiger/AmoMe4SZjfGXkbe3W0DaP_pytorch_lora_weights.safetensors"

def generate_image_with_multiple_loras(prompt):
    try:
        # Make the API call with multiple Lora configurations
        result = fal_client.subscribe(
            "fal-ai/flux-lora",
            arguments={
                "prompt": prompt,
                "loras": [
                    {
                        "path": BRETT_LORA_PATH,
                        "scale": 1
                    },
                    # {
                    #     "path": PEPE_LORA_PATH,
                    #     "scale": 1
                    # },
                    {
                        "path": PONKE_LORA_PATH,
                        "scale": 1
                    }
                ],
                "embeddings": [],
                "image_size": "portrait_16_9",
                "num_inference_steps": 28,
                "guidance_scale": 3.5,
                "enable_safety_checker": True
            }
        )

        # Extract the image URL from the result
        if result and result.get('images') and len(result['images']) > 0:
            return result['images'][0]['url']
        else:
            print("No image URL found in the response")
            return "ERROR"

    except Exception as e:
        print(f"Error generating image: {str(e)}")
        return "ERROR"



# test_prompt = "Brett_memecoin Brett and Ponke_meme, the legendary character, dancing together with exaggerated moves in a vibrant digital space. His expression is full of joy and excitement, showcasing his love for video games. Around him are vivid symbols of partnership and growth, like interlinking circuit nodes and upward arrows, symbolizing the thriving ecosystem. The backdrop is a blue-themed, futuristic cityscape to represent the Base blockchain. Text overlay reads 'Dance through Crypto!' at the top and 'Join the BASE Revolution!' at the bottom"
#
#
# print(generate_image_with_multiple_loras(test_prompt))
