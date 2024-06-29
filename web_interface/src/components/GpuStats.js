import React, { useEffect, useState } from 'react';
import api from '../services/api';

function GpuStats() {
    const [stats, setStats] = useState([]);

    useEffect(() => {
        const fetchStats = async () => {
            const response = await api.getGpuStats();
            setStats(response);
        };

        fetchStats();
    }, []);

    return (
        <div>
            <h2>GPU Stats</h2>
            <ul>
                {stats.map((stat, index) => (
                    <li key={index}>
                        Utilization: {stat.utilization}%, Memory: {stat.memory_used}MB / {stat.memory_total}MB
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default GpuStats;
