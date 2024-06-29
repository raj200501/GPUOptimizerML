import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
    return (
        <header>
            <h1>GPU Optimizer for ML Models</h1>
            <nav>
                <ul>
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/upload">Upload Model</Link></li>
                    <li><Link to="/monitor">Monitor Models</Link></li>
                    <li><Link to="/gpu-stats">GPU Stats</Link></li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;
