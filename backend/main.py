import os
import re
import subprocess
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai
from langchain_openai import AzureChatOpenAI
from gradio_client import Client

# Load environment variables
load_dotenv()
OPENAI_API_VERSION = os.getenv("OPEN_API_VERSION")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Azure OpenAI Client
llm = AzureChatOpenAI(
    azure_deployment="gpt-4",
    openai_api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-12-01-preview"
)

# Helper function to extract the largest Python code block
def extract_largest_code_block(text):
    matches = re.findall(r"```python(.*?)```", text, re.DOTALL)
    return max(matches, key=len).strip() if matches else ""

# Extract Manim class name from Python code
def extract_class_name(code):
    match = re.search(r'class\s+(\w+)\s*\(.*Scene.*\)', code)
    return match.group(1) if match else None

# Generate Manim code with refinement
def generate_manim_code(prompt):
    messages = [{"role": "user", "content": f"Generate Manim code: {prompt}"}]
    response = llm.invoke(messages)
    manim_code = extract_largest_code_block(response.content)
    
    if not manim_code:
        return {"error": "No valid Manim code generated."}

    class_name = extract_class_name(manim_code)
    if not class_name:
        return {"error": "No valid Manim class found."}

    return {"code": manim_code, "class_name": class_name}

# Run Manim script and generate animation
def run_manim_script(manim_code, class_name):
    script_path = "generated_script.py"
    output_path = "static/animation.mp4"
    
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(manim_code)
    
    try:
        subprocess.run(
            ["manim", script_path, class_name, "-o", output_path, "--format=mp4"],
            check=True, capture_output=True, text=True
        )
        return {"video_url": f"/static/animation.mp4"}
    except subprocess.CalledProcessError as e:
        return {"error": f"Manim execution failed: {e.stderr}"}

# API Route to generate Manim animation
@app.route("/api/generate_manim", methods=["POST"])
def generate_manim():
    data = request.json
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Prompt is required."}), 400

    result = generate_manim_code(prompt)
    if "error" in result:
        return jsonify(result), 500
    
    return jsonify(run_manim_script(result["code"], result["class_name"]))

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Server is running!"}), 200


# Sample test route
@app.route("/api/text", methods=["GET"])
def get_text():
    return jsonify({"message": "Hello, World!"})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)