from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
import datetime
import hashlib
import secrets

def hash(password : str, salt : str | None = None) -> str:
    password_bytes : bytes = password.encode('utf-8')
    if salt is None:
        return hashlib.sha512(password_bytes).hexdigest()
    salt_bytes : bytes = salt.encode('utf-8')
    return  hashlib.sha512(password_bytes + salt_bytes).hexdigest()

def generate_aes_key(key_length : int = 32) -> bytes:
    return secrets.token_bytes(key_length)

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SECRET_KEY'] = generate_aes_key().hex()

users = [
    {
        'username' : 'someone@outlook.com',
        'password' : '54c33e6d56bdc0830df3bf77ce71905468445cddec3c013c94dfe81ad4d42999553c05c6cb996c499889e8fa987a360753aa4c341a3d64ab07480a728a20aa96'   
    },
    {
        'username' : 'someone_else@yahoo.com',
        'password' : '0466703d4d76babcb399a107eaa726b95fb6b1b6a0d55e5e292f2c30921e5af830e78cf161269382da79fd6f78bbbcb7ebb85a3384448d0eba4398e7b152dc59'
    }
]

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = hash(data['password'])
    token : str | None = None
    for user in users:
        current_username : str = user['username']
        current_password : str = user['password']
        if username == current_username and password == current_password:
            expiration_time : datetime = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            token : str = jwt.encode({'sub': username, 'exp': expiration_time}, app.config['SECRET_KEY'], algorithm='HS256')
    if token is None:
        return jsonify({'error': 'Invalid credentials'}), 401
    return jsonify({'token': token})

@app.route('/dummy', methods=['GET'])
def dummy():
    token : str = request.headers['Authorization']
    if not token:
        return jsonify({'error': 'Missing token'}), 401
    try:
        payload = jwt.decode(token.split()[1], app.config['SECRET_KEY'], algorithms=['HS256'])
        # response will be some dummy information back
        return jsonify({
            'payload': payload,
            'message': 'Can still use token'
        })
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
