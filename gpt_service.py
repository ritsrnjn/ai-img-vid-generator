import os
import json
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables
load_dotenv()
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

def generate_text(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a creative script writer."},
                {"role": "user", "content": prompt}
            ],
            response_format={
                "type": "text"
            },
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error in generating text: {e}")
        return None


def convert_to_json(response):
    response = response.strip().lstrip('```json').rstrip('```').strip()
    try:
        return json.loads(response)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None


#test
# print(generate_text("Hello please generate a meme for me"))
