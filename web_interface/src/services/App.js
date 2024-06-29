import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './pages/HomePage';
import UploadPage from './pages/UploadPage';
import MonitorPage from './pages/MonitorPage';
import GpuStats from './components/GpuStats';
import Header from './components/Header';
import Footer from './components/Footer';
import './App.css';

function App() {
    return (
        <Router>
            <Header />
            <Switch>
                <Route path="/" exact component={HomePage} />
                <Route path="/upload" component={UploadPage} />
                <Route path="/monitor" component={MonitorPage} />
                <Route path="/gpu-stats" component={GpuStats} />
            </Switch>
            <Footer />
        </Router>
    );
}

export default App;
