# tensorflow-cluster-docker

In this project, I wanted to build a cluster of container to run a tensorflow application.

<!!!> You need to put the docker-compose file into tensorflow folder <!!!!>

I choose to split the work between multiple container to simulate a cluster between multiple computer. We will see hpow our tensorflow application work.

## Folder directory

The src folder get all scripts

The master folder contain the script to create a the server.
The worker folder contain the script to link a worker to the cluster

## Run scripts

In the src folder, we have 2 scripts. The first one is  tensorflow-test. You can test and see that tensorflow train a neural network on a data-set. The second tensorflow-HPC show how we use tensorflow on a cluster to compute a simple operation. The compute will be shared between multiple node of the cluster.

To build the cluster, you need to run:

docker-compose up

It will build the network, run all containers and start the cluster.

After, you need to executer this command on an other terminal to compute a simple operation on the cluster.

docker exec -it tensorflow_master_1 python src/tensorflow-HPC.py

You can change the script by src/tensorflow-test.py to train a neural network on a single machine.
