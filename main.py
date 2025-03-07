from flask import Flask, render_template, request, jsonify
import requests
import os
from prompt_templates import BEER_TASTING_PROMPT

app = Flask(__name__, template_folder='templates', static_folder='static')

API_URL = "https://chat.ivislabs.in/api/chat/completions"
API_KEY = "sk-b9987f2711074d928e675a9be574ede6"  # Replace with actual API key

def send_api_request(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gemma2:2b",  # Default model, update as needed
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    response_data = response.json()
    return response_data.get("choices", [{}])[0].get("message", {}).get("content", "No response received.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    beer_name = request.form.get('beer_name', 'Golden Harvest Amber Ale')
    beer_style = request.form.get('beer_style', 'Pale Ale')
    beer_taste = request.form.get('beer_taste', 'Balanced')
    notes_length = request.form.get('notes_length', 'brief')
    include_food_pairing = request.form.get('include_food_pairing', 'false').lower() == 'true'
    
    prompt = BEER_TASTING_PROMPT.format(
        beer_name=beer_name,
        beer_style=beer_style,
        beer_taste=beer_taste,
        notes_length=notes_length,
        include_food_pairing="Include a food pairing recommendation." if include_food_pairing else ""
    )
    
    try:
        content = send_api_request(prompt)
        
        formatted_response = {
            "status": "success",
            "beer_name": beer_name,
            "beer_style": beer_style,
            "beer_taste": beer_taste,
            "notes_length": notes_length,
            "include_food_pairing": include_food_pairing,
            "tasting_notes": content.strip()
        }
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
    # print(formatted_response)
    return jsonify(formatted_response)

if __name__ == '__main__':
    app.run(debug=True)