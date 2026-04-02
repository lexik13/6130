import subprocess
import time

HADOOP_STREAMING_JAR = "$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar"

input_path = "/bfs/input0"
iteration = 0

start_time = time.time()

while True:
    output_path = f"/bfs/output{iteration}"

    cmd = f"""
    hadoop jar {HADOOP_STREAMING_JAR} \
    -input {input_path} \
    -output {output_path} \
    -mapper mapper.py \
    -reducer reducer.py
    """

    # Run Hadoop job
    process = subprocess.run(cmd, shell=True)

    if process.returncode != 0:
        print("Error running Hadoop job")
        break

    # Check for GRAY nodes
    check_cmd = f"hdfs dfs -cat {output_path}/part-00000 | grep GRAY"
    result = subprocess.run(check_cmd, shell=True, stdout=subprocess.PIPE)

    if not result.stdout:
        break

    input_path = output_path
    iteration += 1

end_time = time.time()

print("Total iterations:", iteration)
print("Execution time: {:.4f} seconds".format(end_time - start_time))