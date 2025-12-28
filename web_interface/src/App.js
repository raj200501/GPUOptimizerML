import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import UploadPage from './pages/UploadPage';
import MonitorPage from './pages/MonitorPage';
import GpuStatsPage from './pages/GpuStatsPage';

function App() {
    return (
        <Router>
            <Header />
            <main>
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/upload" element={<UploadPage />} />
                    <Route path="/monitor" element={<MonitorPage />} />
                    <Route path="/gpu-stats" element={<GpuStatsPage />} />
                </Routes>
            </main>
            <Footer />
        </Router>
    );
}

export default App;
