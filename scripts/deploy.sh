#!/bin/bash

# Build and run backend
cd ../backend_api
docker build -t gpu_optimizer_backend .
docker run -d -p 5000:5000 --name gpu_optimizer_backend gpu_optimizer_backend

# Build and run web interface
cd ../web_interface
docker build -t gpu_optimizer_frontend .
docker run -d -p 3000:3000 --name gpu_optimizer_frontend gpu_optimizer_frontend

# Initialize the database
docker exec -i mysql_container mysql -u root -p<password> < db_init/init.sql
