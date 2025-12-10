import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

# 1. SETUP
app = Flask(__name__)
CORS(app)  # Allows Unity to talk to this server

# TODO: PASTE YOUR GOOGLE AI STUDIO KEY HERE
# Get it from: https://aistudio.google.com/
os.environ["GEMINI_API_KEY"] = "PASTE_YOUR_API_KEY_HERE"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# 2. THE BRAIN (Gemini Model)
model = genai.GenerativeModel('gemini-1.5-pro')

@app.route('/analyze_contract', methods=['POST'])
def analyze():
    try:
        data = request.json
        user_text = data.get('text', '')

        # 3. THE PROMPT (The "Agroww" Persona)
        # We force Gemini to reply in a specific JSON format so Unity can read it.
        prompt = f"""
        You are 'Agroww', an AI Legal Guardian for Indian farmers. 
        Analyze this contract clause or question: "{user_text}"
        
        Identify if there is a risk (Financial, Weather, or Legal).
        
        Strictly output your answer in this JSON format ONLY:
        {{
            "analysis": "A short, simple explanation for a farmer (max 2 sentences).",
            "risk_tag": "TAG_SAFE" or "TAG_DROUGHT" or "TAG_PEST" or "TAG_FINANCIAL"
        }}
        """

        response = model.generate_content(prompt)
        
        # Clean up the response to ensure it's valid JSON
        clean_response = response.text.replace('```json', '').replace('```', '')
        
        print(f"Gemini replied: {clean_response}") # For debugging
        return clean_response

    except Exception as e:
        return jsonify({"analysis": "Error connecting to AI.", "risk_tag": "TAG_SAFE"})

if __name__ == '__main__':
    # Runs the server on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)