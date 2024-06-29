import React, { useEffect, useState } from 'react';
import api from '../services/api';

function ModelMonitor() {
    const [models, setModels] = useState([]);

    useEffect(() => {
        const fetchModels = async () => {
            const response = await api.getModels();
            setModels(response);
        };

        fetchModels();
    }, []);

    return (
        <div>
            <h2>Monitor Models</h2>
            <ul>
                {models.map(model => (
                    <li key={model.id}>
                        {model.name} - {model.status}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ModelMonitor;
