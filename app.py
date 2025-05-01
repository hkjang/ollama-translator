import os
import requests
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434")
OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME", "llama3")
OLLAMA_TRANSLATE_PROMPT = os.getenv("OLLAMA_TRANSLATE_PROMPT", "You are a professional translator. Maintain the tone, context, and style of the original text. Do not explain. Only output the translated text. Translate the following text into {lang}:")

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    if request.method == "POST":
        source_text = request.form.get("text", "")
        target_lang = request.form.get("lang", "en")
        translated_text = translate_with_ollama(source_text, target_lang)
    return render_template("index.html", translated_text=translated_text)

def translate_with_ollama(text, target_lang):
    system_prompt = OLLAMA_TRANSLATE_PROMPT.replace("{lang}", target_lang)
    payload = {
        "model": OLLAMA_MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    }
    response = requests.post(
        f"{OLLAMA_API_URL}/v1/chat/completions",
        headers={"Content-Type": "application/json"},
        json=payload
    )
    if response.status_code == 200:
        translated_text = response.json()["choices"][0]["message"]["content"].strip()
        return translated_text
    else:
        return f"Error: {response.status_code}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
