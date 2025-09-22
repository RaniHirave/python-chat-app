from flask import Blueprint, render_template, request, jsonify

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/')
def index():
    return render_template('index.html')

@chat_bp.route('/send_message', methods=['POST'])
def send_message():
    message = request.json.get('message')
    # Here you would typically handle the message, e.g., save it to a database or broadcast it
    return jsonify({'status': 'success', 'message': message})

@chat_bp.route('/get_messages', methods=['GET'])
def get_messages():
    # This is a placeholder for retrieving messages from a database or in-memory store
    messages = []  # Replace with actual message retrieval logic
    return jsonify(messages)