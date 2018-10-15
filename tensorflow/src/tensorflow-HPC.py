#This programme is show an exemple of how we can use tensorflow in a cluster
import tensorflow as tf

print("Set variable")

x = tf.constant(2)# set a value

with tf.device("/job:cluster/task:1"):
    y2 = x - 66 # compute the value y2 on the cluster on the node with th task number 1

with tf.device("/job:cluster/task:0"):
    y1 = x + 300 # compute the value y1 on the cluster on the node with th task number 0
    y = y1 + y2 # get the value y2 from an other node of the cluster


with tf.Session("grpc://tensorflow_master_1:2222") as sess:
    print("In Session") #print that the master create a session
    result = sess.run(y) #run the compute and get the resulte
    print("Your result :")
    print(result) #print the resulte
