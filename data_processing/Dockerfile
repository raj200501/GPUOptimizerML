FROM openjdk:8-jdk-slim

WORKDIR /app

COPY . .

CMD ["spark-submit", "--master", "local", "spark_jobs/data_transformation.py"]
