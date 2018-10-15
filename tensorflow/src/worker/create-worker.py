import sys
task_number = int(sys.argv[1])

import tensorflow as tf

cluster = tf.train.ClusterSpec({
    "cluster": [
        "tensorflow_worker-1_1:2222",
        "tensorflow_master_1:2222",
        "tensorflow_worker-2_1:2222"
    ]})

server = tf.train.Server(cluster, job_name="cluster", task_index=task_number)

print("Starting server #{}".format(task_number))

server.join()
