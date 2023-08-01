# 五、POD service and communication


### 1. Service and port

The service is actually easy to understand. Think about it, how do you manage a group of the same POD? Do you need to know all their IPs, and then manually configure and connect them one by one? Obviously not needed, how to solve this problem, use services, services are actually equivalent to a routing function.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6vz9tf8wej30mf0dnq60.jpg" style="zoom:200%;" />

Look at this, there are 3 PODs on the front end, and a Backend, how to make the whole system run normally, using services. The three front-ends set up a front-end service to expose an IP, and the Backend does the same to expose a service, so each part of the connection only focuses on the service IP, regardless of the network information of each POD.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6vz9trl8vj30i707bjsq.jpg" style="zoom:200%;" />

This is the YAML for creating a service, KIND is a Service, and then maps the port of the POD, as well as a label selector. Services can be created with kubectl expose or kubectl create.

![1568172425531](<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6vz9ubj81j30px0dwn2q.jpg" style="zoom:200%;" />

Is this fun? It is to test whether the POD can be accessed through the service. It is to exec to a POD first, and then access the ip of this service through curl to see if it can connect to other PODs. It's very simple.

Let’s talk about ports. A POD can have one port or multiple ports, which is easy to understand.



### 2. Service Discovery

In fact, it is to use environment variables to connect to this service instead of using a fixed IP. After all, the IP may change. You can select a POD, then kubectl exec kubia-3inly env to list the environment variables, then view the environment variables of this service, and provide other client connections through variables.



### 3. Endpoint

This guy is more interesting. Look at the picture.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6vz9v2ldhj30sm0c67e1.jpg" style="zoom:200%;" />

It's very clear. It's equivalent to mapping the service to two Endpoints. Can it be understood as load balancing? It's a bit like that.



### 4. The method of exposing the service to external clients

Remember, three methods.

- [ ] NodePort

   > I don’t know the meaning of this setting. What does it mean? It is equivalent to reserving a PORT for all nodes, and then you have two ways to access it. The first is clusterIp: port, the second is nodeIp: port
   >
   > ![https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6vz9w5kr5j30kl08hac7.jpg](https://p.ipic.vip/c9q21r.jpg)
   >
   >  has three port numbers, the first is the port of the service cluster, The second is the target port of the POD, and the third is the nodePort port. ![](https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6vz9x1ii4j30pg0j845q.jpg) As you can see from this picture, 30123 is the port of nodeport, through this port Add the IP of node to access the node.

- [ ] load balancing method

   > It uses an external IP from the cloud infrastructure, which is a unique and publicly accessible IP address, through which it is redirected to the service. There is nothing else to say about other feelings, just watch this.
   >
   > ![1568194400337](<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6vz9y0p7gj30ew06vmyh.jpg" style="zoom:200%;" />This loads A balancer can average traffic and see what its policy is.

- [ ] ingress

   > A picture to see its function:
   >
   > ![1568195843695](<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6vz9yhuk1j30p808oadh.jpg" style="zoom:200%;" />What do you mean Well, that is to say, you can selectively access services through domain names.
   >
   > ![1568195964547](<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6vz9yz6fkj30nb0aswji.jpg" style="zoom:200%;" />This The picture shows how to access POD through ingress.

  

### 5. Readiness Probe

Another fucking amazing thing. It really needs to deal with various situations. The readiness probe is used to deal with this kind of situation. That is, when you start a POD, it is impossible to get it up immediately, but kube doesn’t know it. It may still give you the traffic. , So how to avoid this problem, use the ready pointer, that is to say, set a pointer to notify kube of success or failure.

![1568196997031](<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6vzg9qd9bj30hz0baabc.jpg" style="zoom:200%;" />

A ready pointer is set, which is to execute the ls command in the container to see if the file exists.
