import React from "react";
import { Link } from "react-router-dom";
import "./navbarStyles.css";

function Navbar() {
  return (
    <header className="navbar">
      <nav>
        <Link to="/">Home</Link>
        <Link to="/login">Login</Link>
        <Link to="/register">Register</Link>
      </nav>
    </header>
  );
}

export default Navbar;
