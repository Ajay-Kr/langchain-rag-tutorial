from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
from query_data import answer_query

# Load environment variables from .env file
load_dotenv()

# Access the API key
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize Flask app
app = Flask(__name__)

# Endpoint for answering queries
@app.route('/api/query', methods=['GET'])
def query_endpoint():
    query_text = request.args.get('query')

    if not query_text:
        return jsonify({'error': 'Query parameter is required'}), 400

    response = answer_query(query_text)
    formatted_response = f"Respone: {response}"
    print(formatted_response)
    return jsonify({'query': query_text, 'response': response})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
