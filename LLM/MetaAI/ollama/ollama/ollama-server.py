from flask import Flask, request, jsonify
import requests
import json
app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434"

import logging

logging.basicConfig(level=logging.DEBUG)


@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        # Get the input from the request
        data = request.json
        prompt = data.get('prompt', '')
        model = data.get('model', 'deepseek-llm:7b')  # Default model
        # model = data.get('model', 'qwen2.5-coder:latest')  # Default model
        # model = data.get('model', 'llama2:latest')  # Default model

        
        

        logging.debug(f"Received prompt: {prompt}")

        # Forward the request to Ollama
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={"model": model, "prompt": prompt},
            stream=True  # Handle streaming response
        )

        logging.debug("Processing streaming response from Ollama")

        # Collect the streaming chunks and parse them
        output = ""
        for chunk in response.iter_lines(decode_unicode=True):
            if chunk:
                # Ensure each chunk is valid JSON and extract 'response'
                try:
                    chunk_json = json.loads(chunk)
                    output += chunk_json.get('response', '')
                except json.JSONDecodeError:
                    logging.warning(f"Failed to decode chunk: {chunk}")

        logging.debug(f"Ollama response: {output}")

        # Return the final output
        return jsonify({"response": output})

    except Exception as e:
        logging.exception("Error occurred in /api/generate")
        return {"error": str(e)}, 500




if __name__ == '__main__':
    app.run(port=5000, debug=True, use_reloader=True)


