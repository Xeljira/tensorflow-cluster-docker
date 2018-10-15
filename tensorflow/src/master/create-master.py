import sys
import tensorflow as tf

task_number = int(sys.argv[1])

cluster = tf.train.ClusterSpec({
    "cluster": [
        "tensorflow_worker-1_1:2222",
        "tensorflow_master_1:2222",
        "tensorflow_worker-2_1:2222"
    ]})#set the ip for the cluster

server = tf.train.Server(cluster, job_name="cluster", task_index=task_number)

print("Starting server #{}".format(task_number)) #get the number of the server

server.join() #join the server
server.start() #start the server
