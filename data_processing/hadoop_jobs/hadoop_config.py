import os
from pyhdfs import HdfsClient
from subprocess import call

HADOOP_HOME = os.getenv('HADOOP_HOME', '/usr/local/hadoop')
HDFS_URL = os.getenv('HDFS_URL', 'http://localhost:50070')
HDFS_USER = os.getenv('HDFS_USER', 'hdfs')

# Set up the HDFS client
client = HdfsClient(hosts=HDFS_URL, user_name=HDFS_USER)

# Define paths
LOCAL_INPUT_PATH = '../data/sample_data.csv'
HDFS_INPUT_PATH = '/user/hadoop/sample_data.csv'
HDFS_OUTPUT_PATH = '/user/hadoop/output'

def upload_to_hdfs():
    if not client.exists(HDFS_INPUT_PATH):
        client.copy_from_local(LOCAL_INPUT_PATH, HDFS_INPUT_PATH)
        print(f"Uploaded {LOCAL_INPUT_PATH} to {HDFS_INPUT_PATH}")
    else:
        print(f"{HDFS_INPUT_PATH} already exists")

def run_hadoop_job():
    # Clear previous output if exists
    if client.exists(HDFS_OUTPUT_PATH):
        client.delete(HDFS_OUTPUT_PATH, recursive=True)
        print(f"Deleted existing HDFS output directory: {HDFS_OUTPUT_PATH}")

    # Define the Hadoop streaming command
    hadoop_streaming_jar = os.path.join(HADOOP_HOME, 'share/hadoop/tools/lib/hadoop-streaming-*.jar')
    mapper = 'mapper.py'
    reducer = 'reducer.py'

    command = [
        'hadoop', 'jar', hadoop_streaming_jar,
        '-input', HDFS_INPUT_PATH,
        '-output', HDFS_OUTPUT_PATH,
        '-mapper', f'python {mapper}',
        '-reducer', f'python {reducer}'
    ]

    # Execute the Hadoop streaming job
    call(command)
    print("Hadoop streaming job completed")

def configure_hadoop():
    upload_to_hdfs()
    run_hadoop_job()

if __name__ == "__main__":
    configure_hadoop()
