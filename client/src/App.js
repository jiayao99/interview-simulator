import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./Navbar";
import LoginForm from "./LoginForm";
import RegisterForm from "./RegisterForm";
import "./styles.css";



function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/login" element={<LoginForm />}></Route>
        <Route path="/register" element={<RegisterForm />}></Route>
      </Routes>
    </Router>
  );
}

export default App;
