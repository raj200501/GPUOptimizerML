import React, { useState } from 'react';
import api from '../services/api';

function ModelUpload() {
    const [file, setFile] = useState(null);

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleFileUpload = async () => {
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await api.uploadModel(formData);
            alert(response.message);
        } catch (error) {
            alert('Error uploading file');
        }
    };

    return (
        <div>
            <h2>Upload Model</h2>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleFileUpload}>Upload</button>
        </div>
    );
}

export default ModelUpload;
