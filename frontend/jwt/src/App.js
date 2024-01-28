import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [token, setToken] = useState('');
  const [message, setMessage] = useState('');

  const handleLogin = async () => {
    try {
      console.log(`username: ${username}, password: ${password}`)
      const response = await axios.post('http:///192.168.1.100:7000/login', { username, password });
      setToken(response.data.token);
      setMessage('');
    } catch (error) {
      setToken('');
      setMessage('Invalid credentials');
    }
  };

  const handleProtectedRequest = async () => {
    try {
      const response = await axios.get('http:///192.168.1.100:7000/dummy', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      if(response.status === 200) {
        const data = response.data;
        setMessage(`payload: ${JSON.stringify(data.payload)}, message: ${JSON.stringify(data.message)}`);
      }
      else {
        setMessage(`Status code: ${response.status}`)
      }
    } catch (error) {
      setMessage('Unauthorized access');
    }
  };

  return (
    <div>
      <h1>JWT Authentication Example</h1>
      <div>
        <label>Username: </label>
        <input type="text" value={username} onChange={(e) => setUsername(e.target.value) } />
      </div>
      <div>
        <label>Password: </label>
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value) } />
      </div>
      <div>
        <button onClick={handleLogin}>Login</button>
      </div>
      {token && (
        <div>
          <h2>Protected Resource</h2>
          <button onClick={handleProtectedRequest}>Access Protected Resource</button>
          <p>{message}</p>
        </div>
      )}
    </div>
  );
}

export default App;

