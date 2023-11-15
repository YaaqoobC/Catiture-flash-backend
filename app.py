# to activate the vm
    # --> source venv/bin/activate
# to activate the Flask Backend
    # run this file
    # --> python3 app.py

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json  # Get form data from the request

    # Process the form data (customize based on your needs)

    # Assuming the form submission is successful

    print(f"Received Payload:\n"
      f"Name: {data['name']}\n"
      f"Email: {data['email']}\n"
      f"Message: {data['message']}")



    return jsonify({'success': True, 'message': 'Form submitted successfully!'})
@app.route('/')
def home():
    return 'Welcome to the Catiture Flask App!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)







