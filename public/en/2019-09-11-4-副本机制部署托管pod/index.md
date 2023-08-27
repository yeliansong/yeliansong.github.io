# 四、Deploy managed POD by copy mechanism


### 1. Survival Probe

Why come up with such a profound word? We know that if a container program in the POD crashes, kubenetes will restart the program, but the problem is, if it is not a crash, such as a deadlock, or throwing an exception, etc., what to do at this time, kubenetes does not know Whether your container is normal or not, you need to use a probe at this time. In fact, the reason is very simple, that is, use a probe to detect it from time to time to see if it is normal.

Three kinds of probes: 1) HTTP GET probe, which is used to check whether the network is normal. 2) The TCP socket probe is similar, it is to establish a TCP connection, if it succeeds, it is normal. 3) The Exec probe is to execute any command in the container, and if it returns normally, it is successful.

A probe is actually a POD, and some attributes can be defined to control some operations of the probe.



### 2. ReplicationController

It is also a very powerful thing, that is, copy control. It is used to ensure the number of PODs and can be used for horizontal expansion of PODs.

RC has three parts: label selector, label selector, used to determine which PODs are in the RC scope; RC COUNT: used to specify the number of PODs; POD TEMP: template, to create a new copy of POD.

Let's take a look at the impact of tags on RC. In fact, it is easy to understand that RC is only responsible for the tags defined in it, and monitors the number of PODs of these tags at all times. When the POD of these tags decreases or increases, it will dynamically adjust. So, there are two situations, the first one, if you modify the label in the running POD, it means that the POD used to belong to A, and then it belongs to B later. At this time, RC has to do something, and he will recreate the POD . In the second case, if you modify the label of RC, then all the PODs in this label will be out of monitoring, and all of them will be free.

Play around with kubectl edit rc kubia, and you will find that you can modify the current RC, and then modifying the current RC will have no effect on the currently running POD, but will only affect the subsequent POD.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6vz9qkq36j30h90ab76n.jpg" style="zoom:200%;" />

Interesting, three PODs, after deleting the RC, these three PODs will not be affected, and they will be freed from the shackles of the RC.

But, don't use RC, use ReplicaSet, this buddy has the same function as RC, but the function has been enhanced a lot, mainly because the use of tags is more flexible, and the others are exactly the same as RC, so don't stress about this.



### 3. DaemonSet

What is this used for? It is used to control the deployment of POD, which means to deploy POD according to its own definition.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6vz9rj59cj30mc0d4jxi.jpg" style="zoom:200%;" />

Come, come, look at this product. The ReplicaSet is used on the left. The deployed PODs are disorganized on each node. Now I require only one POD to be deployed on each node. How to deal with this situation? This will use DaemonSet.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6vz9shyq4j30jr0acdhl.jpg" style="zoom:200%;" />

This is the YAML file of DaemonSet, nodeSelector node scheduler.



### 4. JOB

This is used to define a task, which is to end after completion. Rather than hoping to run it all the time, this is also a good use. JOB also has a lot of application settings, you can set the delay time of the task and so on.
