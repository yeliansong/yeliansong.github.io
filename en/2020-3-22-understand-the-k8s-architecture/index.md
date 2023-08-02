# Understand The K8S Architecture


### 1. k8s components architecture.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images00831rSTgy1gd2v5xofmoj31iv0u0n7a.jpg" style="zoom:200%;" />

Okay,  it's very easy to understand. Like above, master node is the most important. It controls the other nodes to join the cluster. Also API server is exposed outside. Through the master node, then can arrange the other nodes.

### 2. Practice

#### Target: Create the k8s cluster, then deploy the application to these 2 nodes.

#### Steps.

- Use kubeadm init to create the master k8s cluster, then join node1 and node2 to the cluster.

- In the master node, deploy the application with replications as 2.

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images00831rSTgy1gd2wbfwqq3j31fe0460u9.jpg" style="zoom:200%;" />

- After execute that, deployment is completed. You can execute command "kubectl get pods", show the deployment.

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images00831rSTgy1gd2wc6ysd1j321c044q4u.jpg" style="zoom:200%;" />

  The application is deployed separately in the 2 nodes.  

### 3. Understand the process

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images00831rSTgy1gd2vq6vm42j313s0u01co.jpg" style="zoom:200%;" />

This is the whole process. 

When you execute "kubectl run", will call the API Server, then API Server notice the Controller Server to create the deployment resource. After that, Schedule service will arrange the tasks to the node1 and node2. In the node1 and node2, kubelet will create the pods according to the tasks. Kube-proxy will arrange the network config for these 2 nodes. 




