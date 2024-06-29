from pyspark.sql import SparkSession

def analyze_data(input_path):
    spark = SparkSession.builder.appName("DataAnalysis").getOrCreate()

    # Load data
    data = spark.read.csv(input_path, header=True, inferSchema=True)

    # Perform analysis
    age_count = data.groupBy("age").count()
    avg_salary = data.agg({"salary": "avg"})

    # Show results
    age_count.show()
    avg_salary.show()

if __name__ == "__main__":
    input_path = "../data/sample_data.csv"
    analyze_data(input_path)
