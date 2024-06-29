from pyspark.sql import SparkSession

def aggregate_data(input_path, output_path):
    spark = SparkSession.builder.appName("DataAggregation").getOrCreate()

    # Load data
    data = spark.read.csv(input_path, header=True, inferSchema=True)

    # Aggregate data
    aggregated_data = data.groupBy("age").agg({"salary": "avg"})

    # Save aggregated data
    aggregated_data.write.csv(output_path, header=True)

if __name__ == "__main__":
    input_path = "../data/sample_data.csv"
    output_path = "../data/aggregated_data.csv"
    aggregate_data(input_path, output_path)
