import React, { useState } from "react";
import axios from 'axios';

import "./formStyles.css";

function RegisterForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        const response = await axios.post('http://127.0.0.1:5000/register', { email, password });
        console.log(response);
        // Additional logic on successful registration
    } catch (error) {
        console.error('Registration error:', error.response);
        // Handle errors (e.g., display error message to user)
    }
};

  return (
    <header className="form-container">
      <div>
        <h2>Register</h2>
        <form onSubmit={handleSubmit}>
          <div>
            <label>Email:</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div>
            <label>Password:</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit">Register</button>
        </form>
      </div>
    </header>
  );
}

export default RegisterForm;
