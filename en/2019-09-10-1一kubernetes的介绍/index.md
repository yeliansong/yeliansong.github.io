# 一、Introduction to Kubernetes



### 1. Comparison between monolithic applications and microservices

Disadvantages of monolithic applications: run on several servers in the form of a single process or several processes, the deployment cycle is long, and the operation and maintenance and development are disconnected. After the developers complete the development, they are packaged into a whole for operation and maintenance deployment.

There is no decoupling between modules. To modify a module, the whole package needs to be deployed.

The advantages of microservices: decoupling between modules, shortening the deployment cycle, and a single module can achieve independent development, deployment, upgrade, and scaling. Reduce deployment time. In addition to saving resources, modules can be separated
  Scale up all of them, not all of them.



### 2. DevOps

Microservices brought about DevOps. The previous team combination was that after the developers completed the development, they gave the results to the operation and maintenance, and then the operation and maintenance completed the deployment, and the development and operation and maintenance were completely separated. This brings about a problem. Developers cannot understand the needs of users at the first time, and they do not understand the operating environment of the system, and the operation and maintenance do not understand the functions of the product. After the advent of microservices, through the virtualization of system hardware resources by kubernetes, developers do not have to worry about the deployment environment, simplifying system deployment, developers can also participate in the deployment, and DevOps is derived.


### 3. Container technology

Container technology is actually the isolation technology of Linux. Isolation by what? Namespaces and CGROUPs. Namespaces are used to isolate different processes, and CGROUPs are used to isolate resources. It is through this that a host can run multiple different applications. Two applications on the same host can also share files. If they share the same basic image, they share resources. However, files at this layer are read-only. If they are overwritten and written, they are written on the basis of the basic image. A layer of files, the container is a joint file system.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6ur4b89noj30f708qq5w.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6ur7hcbvdj309f0h5n02.jpg" style="zoom:200%;" />

### 4. Porting of containers

The image of the container is a complete system, which has been trimmed. What it cuts is still the host machine, so whether a container image can run or not depends on the environment in which the image is running. If the kernel version of the host environment where the image is orchestrated is consistent with the operating environment, it can run. At the same time, it also depends on whether some system resources unique to the host are used.



### 5. Kubernetes

Google came up with this thing to solve the management deployment problem of Google's tens of thousands of servers. After the container technology became popular, Kubernetes supported containers, so it can be said that Kubernetes has made Docker. Let's be consistent. The design purpose of Kubernetes is to abstract the underlying infrastructure and provide you with a master node to manage thousands of running nodes of your service. You don't have to care about the deployment of your service running nodes.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6ur4cniqdj30eg05lac3.jpg" style="zoom:150%;" />



### 6. The composition of Kubernetes

Master node: API server (function entry, management of other modules), Schedule (scheduling application), Control Manager, etcd (distributed data storage)

Working node: kubelet (communicating with API, managing containers), kube-proxy (responsible for network traffic balancing)

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6ur7idxf5j30ey05xgo0.jpg" style="zoom:150%;" />
