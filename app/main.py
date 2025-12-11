from flask import Flask, render_template, request, jsonify
from datetime import datetime, timezone
import os
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/time')
def get_time():
    return jsonify({'current_time': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')})

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        if not name or not email:
            return jsonify({'error': 'Name and email are required'}), 400
        
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$', email):
            return jsonify({'error': 'Invalid email format'}), 400
            
        return jsonify({'message': f'Thanks {name}! We received your message.'})
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 'yes', 'on'))