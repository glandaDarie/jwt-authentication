# JWT Authentication Example with Flask and React

## Backend (Flask)

### Overview

This example demonstrates JWT authentication using Flask for the backend. Users can log in and receive a JWT, which is then used to access a protected resource.

### Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
  
3. **Run the Flask App:**
   ```bash
   python your_flask_app.py

### Endpoints

/login

Method: POST
Description: Authenticates users and generates a JWT.
Request Body:

{
    "username": "user@example.com",
    "password": "user_password"
}

Response:
200 OK with a JWT token on successful authentication.
401 Unauthorized with an error message on invalid credentials.

/dummy

Method: GET
Description: Demonstrates access to a protected resource using a valid JWT.
Request Headers:
Authorization: Bearer <JWT_TOKEN>
Response:
200 OK with dummy information on successful access.
401 Unauthorized with an error message on invalid or expired token.

### Configuration
Ensure to replace 'your-secret-key' with a strong, unique secret key for enhanced security.

### User Credentials
Replace the example user credentials in the users list with your actual user data.

## Frontend

### Overview
The React frontend interacts with the Flask backend to demonstrate the JWT authentication flow. Users can enter credentials, log in, and access a protected resource.

### Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo/frontend

2. **Run the React App:**
   ```bash
   npm start

3. **Enter Credentials:**
  Enter your username and password.

4. **Access Protected Resource:**
  Once logged in, click the "Access Protected Resource" button to demonstrate access to a protected API endpoint using the obtained JWT.
