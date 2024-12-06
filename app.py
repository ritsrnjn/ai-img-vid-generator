from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from onlycalls.controller import onlycalls_controller

load_dotenv() 

app = Flask(__name__)
CORS(app)

# Register the blueprint
app.register_blueprint(onlycalls_controller, url_prefix='/onlycalls')

@app.route('/')
def index():
   return "Hello, World!"

if __name__ == '__main__':
   port = int(os.getenv('PORT', 8080))  # Default to 5000 if not found
   app.run(host='0.0.0.0', port=port, debug=True)
