import os
from openai import OpenAI
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ ERROR: OPENAI_API_KEY is not set! Check your environment variables.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Initialize Flask app
app = Flask(__name__)

def get_openai_response(user_prompt):
    """Function to get response from OpenAI API"""
    try:
        print("⚡ Sending request to OpenAI...")
        print(f"📨 Prompt: {user_prompt}")
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[{"role": "user", "content": user_prompt}],
            max_tokens=1000,
            temperature=0.7
        )
        print("✅ Received response from OpenAI")
        return response.choices[0].message.content
    except Exception as e:
        print(f"❌ Error while calling OpenAI: {str(e)}")
        return f"Error: {str(e)}"

@app.route('/chat', methods=['POST'])
def chat():
    """API Endpoint to handle chat requests"""
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = get_openai_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    print("🚀 Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True)
