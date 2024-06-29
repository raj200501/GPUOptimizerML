from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def transform_data(input_path, output_path):
    spark = SparkSession.builder.appName("DataTransformation").getOrCreate()

    # Load data
    data = spark.read.csv(input_path, header=True, inferSchema=True)

    # Transform data
    transformed_data = data.withColumn("salary", col("salary") * 1.1)

    # Save transformed data
    transformed_data.write.csv(output_path, header=True)

if __name__ == "__main__":
    input_path = "../data/sample_data.csv"
    output_path = "../data/transformed_data.csv"
    transform_data(input_path, output_path)
