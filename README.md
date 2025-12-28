# GPU Optimizer for ML Models

Welcome to the GPU Optimizer for ML Models! This project aims to optimize GPU performance for machine learning models, leveraging advanced techniques and a wide array of technologies.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)

## Introduction
The GPU Optimizer for ML Models is a comprehensive platform designed to improve GPU performance for training and deploying machine learning models. This platform features a web-based interface for managing and monitoring models, an API for integration, and robust backend services for data processing and model optimization.

## Features
- **GPU Performance Optimization**: Improve GPU utilization for training ML models using advanced scheduling and resource management.
- **Model Management**: Upload, manage, and monitor ML models through a web-based interface.
- **Data Processing**: Use Spark, Hadoop, and other big data technologies for data transformation and analysis.
- **Real-time Monitoring**: Monitor GPU utilization and performance in real-time.
- **Secure API**: Securely manage models and GPU resources via a robust API.

# Project Structure

The GPU Optimizer for ML Models project is organized into several directories and files, each serving a specific purpose. Below is a detailed breakdown of the project structure:

```plaintext
MLGpuOptimizer/
├── backend_api/
│   ├── config/
│   │   └── config.py
│   ├── controllers/
│   │   ├── model_controller.py
│   │   └── gpu_controller.py
│   ├── models/
│   │   └── model.py
│   ├── routes/
│   │   └── api_routes.py
│   ├── services/
│   │   ├── gpu_service.py
│   │   └── model_service.py
│   ├── utils/
│   │   └── optimization.py
│   ├── app.py
│   └── Dockerfile
├── data_processing/
│   ├── spark_jobs/
│   │   ├── data_transformation.py
│   │   ├── data_aggregation.py
│   │   └── data_analysis.py
│   ├── hadoop_jobs/
│   │   └── hadoop_config.py
│   ├── utils/
│   │   └── spark_utils.py
│   └── Dockerfile
├── web_interface/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.js
│   │   │   ├── Footer.js
│   │   │   ├── ModelUpload.js
│   │   │   ├── ModelMonitor.js
│   │   │   └── GpuStats.js
│   │   ├── pages/
│   │   │   ├── HomePage.js
│   │   │   ├── UploadPage.js
│   │   │   └── MonitorPage.js
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.js
│   │   ├── index.js
│   │   └── App.css
│   └── Dockerfile
├── db_init/
│   └── init.sql
├── scripts/
│   └── deploy.sh
├── README.md
```
## Installation

### Prerequisites
- Docker
- Node.js and npm
- Python and pip
- MySQL

### Steps
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/MLGpuOptimizer.git
   cd MLGpuOptimizer
2. **Build and Run Backend:**
   cd backend_api
docker build -t gpu_optimizer_backend .
docker run -d -p 5000:5000 --name gpu_optimizer_backend gpu_optimizer_backend
3. **Build and Run Web Interface:**
cd ../web_interface
docker build -t gpu_optimizer_frontend .
docker run -d -p 3000:3000 --name gpu_optimizer_frontend gpu_optimizer_frontend
4. **Inititalize Database:**
docker exec -i mysql_container mysql -u root -p<password> < db_init/init.sql

## Usage

This guide provides instructions on how to use the GPU Optimizer for ML Models.

### Main Dashboard

1. **Access the Web Interface:**
   - Open your browser and navigate to `http://localhost:3000`.

2. **Navigate the Dashboard:**
   - Use the navigation menu to access different sections of the application.

### Uploading and Monitoring Models

1. **Upload Model:**
   - Navigate to the "Upload Model" section.
   - Click the "Choose File" button and select the model file to upload.
   - Click the "Upload" button to upload the model.

2. **Monitor Models:**
   - Navigate to the "Monitor Models" section.
   - View the list of uploaded models and their status.
   - Each model entry shows the model name and its current status (e.g., uploaded, optimized).

### Viewing GPU Stats

1. **GPU Stats:**
   - Navigate to the "GPU Stats" section.
   - View real-time GPU utilization and memory statistics.
   - The stats include GPU utilization percentage, total memory, free memory, and used memory.

### Example Usage Scenarios

### Scenario 1: Optimizing a New Model

1. **Upload Your Model:**
   - Go to the "Upload Model" section.
   - Select your model file (e.g., a PyTorch model file) and upload it.
   - Wait for the upload to complete and check the model status in the "Monitor Models" section.

2. **Monitor Optimization:**
   - Once the model is uploaded, the system automatically starts optimizing the model.
   - You can monitor the optimization process in the "Monitor Models" section.
   - The status will change from "uploaded" to "optimized" once the optimization is complete.

### Scenario 2: Checking GPU Performance

1. **Access GPU Stats:**
   - Go to the "GPU Stats" section.
   - View real-time statistics of GPU performance, including utilization and memory usage.
   - Use this information to ensure that your GPUs are being utilized efficiently and identify any potential bottlenecks.

For more detailed instructions and troubleshooting, refer to the [FAQ](#faq) section below.

### FAQ

### How do I reset the database?
   - To reset the database, you can re-run the database initialization script:
     ```sh
     docker exec -i mysql_container mysql -u root -p<password> < db_init/init.sql
     ```

### What types of model files are supported?
   - Currently, the platform supports PyTorch model files. Support for other model types can be added by extending the backend services.

### How can I contribute to this project?
   - Contributions are welcome!

If you have any further questions or need assistance, feel free to reach out to the project maintainers.

Happy coding!

## ✅ Verified Quickstart (Local, no Docker)

These steps were verified in a clean environment without Docker by running the backend locally and using SQLite for persistence.

```sh
python -m pip install -r backend_api/requirements.txt
./scripts/run_backend.sh
```

Then visit:
- API base: `http://localhost:5000/api`
- GPU stats: `http://localhost:5000/api/gpu/stats`

To run the React web interface locally (requires Node.js + npm with registry access):

```sh
cd web_interface
npm install
npm start
```

## Smoke Test

Run a basic API verification:

```sh
./scripts/smoke_test.sh
```

## ✅ Verified Offline Demo (No External Dependencies)

If you need a fully runnable, dependency-free demo (no Docker, no pip, no npm), use the built-in demo server:

```sh
./scripts/run_demo.sh
```

Then open `http://localhost:8080` to access the demo dashboard with upload, monitor, and GPU stats panels.

To verify the demo server automatically:

```sh
./scripts/smoke_test_demo.sh
```

The demo server uses the same API paths (`/api/model/upload`, `/api/model/monitor`, `/api/gpu/stats`) and stores data in `backend_api/demo.db`.

## Troubleshooting

- **Docker not available**: If `docker --version` fails, use the Verified Quickstart above to run locally.
- **No GPU / `nvidia-smi` missing**: The `/api/gpu/stats` endpoint returns a zeroed placeholder with a note.
- **Torch/TensorRT not installed**: Model optimization falls back to a safe copy and still marks the model as optimized.
- **Database connection errors**: By default, the backend uses SQLite at `backend_api/gpu_optimizer.db`. You can override with `DATABASE_URL` or `SQLALCHEMY_DATABASE_URI`.
- **No dependency environment**: Use `./scripts/run_demo.sh` to run a full demo without Docker, pip, or npm.


   
   
