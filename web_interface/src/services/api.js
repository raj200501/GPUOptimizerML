import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

const uploadModel = async (formData) => {
    const response = await axios.post(`${API_URL}/model/upload`, formData);
    return response.data;
};

const getModels = async () => {
    const response = await axios.get(`${API_URL}/model/monitor`);
    return response.data;
};

const getGpuStats = async () => {
    const response = await axios.get(`${API_URL}/gpu/stats`);
    return response.data;
};

export default {
    uploadModel,
    getModels,
    getGpuStats
};
