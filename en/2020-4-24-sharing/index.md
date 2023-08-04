# Cloud Tech,Container And K8S Sharing


# Part 1:

For this part, comprise of the basic knowledges including Cloud history, container technology and k8s etc.

## 1. Cloud  Technology

### 1.1 The History Of Cloud computing

​		[https://skyao.io/learning-cloudnative/introduction/history.html]()

- IaaS: Infrastructure as a service

- PaaS: Platform as a service

- SaaS: Software as a service

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdyavrtx33j315t0u0ndg.jpg" style="zoom:200%;" />

### 1.2 Cloud Native

​			[https://skyao.io/learning-cloudnative/introduction/background.html](https://skyao.io/learning-cloudnative/introduction/background.html)

### 1.3 DevOps And Strengths

​            [https://www.qikegu.com/docs/4262](https://www.qikegu.com/docs/4262)

​			[https://skyao.io/learning-cloudnative/devops/](https://skyao.io/learning-cloudnative/devops/)

## 2. Container Technologies

#### 2.1 Virtualization Technology

Virtualization refers to the act of  creating a virtual version of something, including virtual computer hardware platforms, storage devices, and computer network resources etc. It's that let u create useful IT services using resources that are traditionally bond to hardware,  allows you to use physical machine's full capacity by distributing its capabilities among many users or environment.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdyyrcui4pj30vi072abp.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdyys2rfejj315007ugn1.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdyyz7cw72j30t20cg0ul.jpg" style="zoom:200%;" />

### 2.2 VM vs Container 

- **VM: Virtual Machine**

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdyz7hbm2aj31380mstb7.jpg" style="zoom:200%;" />

-  **Container**

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdyzobodq1j312a0jakjl.jpg" style="zoom:200%;" />



<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdyzsk2mhrj30wi0ieaca.jpg" style="zoom:200%;" />

Compare Container with VM

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdz2fu0w9jj313w0ni0vh.jpg" style="zoom:200%;" />

​	**The advantages of using Container:**

- Container is much more lightweight, it is similar to a single isolated process running in the host OS.
- Container start up more faster than VM.
- Container is more suited to micro service.

### 2.3 Docker

Docker is a startup company in the San Francisco based on container technology. It's the best practice of the container technology. Then it becomes the standard as competing with other corporations. Docker is on behalf of container technology.

## 3. Mircoservices

### 3.1 Monolithic Single Application

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdz9039dlmj30f80lajsx.jpg" style="zoom:100%;" />

Monolithic app is the traditional deployment design model. Refer to the above picture, the number of processes depend on each other. The weakness also is visible.it is fussy to deploy the the whole system. It's risky when you upgrade the single application. Because it was connected with other parts. In addition, it's difficult to separate the developer and operation jobs, the developers sometimes need to care about the administration's issue, and system operation staff also needs to locate whether it's the software issues.

### 3.2 Microservices

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdzaf61qs1j31e40s2qj8.jpg" style="zoom:200%;" />

 The above picture is very vivid to express the scope of Microservices. 

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdzas1nrvjj30zc0fk767.jpg" style="zoom:200%;" />

From Monolithic application to micro services application.

Microservices are a software development technique-- that arranges an application as a collection of loosely coupled service. In the micro services architecture, the services are fine-grained and the protocol are lightweight.

- Easier to build and maintain apps.
- Flexibility in using technologies and Scalability
- Easy integration and automatic deployment with Continuous integration tools such as Jenkins. Also enables continuous delivery.
- Improve the efficiency of developing. Reduce the cost in the communication between different teams.
- Code for different service can be written in different languages. Break down the barriers of different languages and technologies.

## 4. Kubernetes

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdzc0dus8ej31cj0u07wj.jpg" style="zoom:200%;" />



[https://www.infoq.cn/article/U2a_7ekuvhmb7dSNp27V](https://www.infoq.cn/article/U2a_7ekuvhmb7dSNp27V)



# Part 2:

This part is the k8s details. Will introduce the k8s key points and some practices. 

## 1. K8S Appetizer

### 1.1  Understanding The Architecture Of K8S Cluster

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdzgd32o49j314c0f40ub.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdzgem5svuj312y0fu41d.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/00831rSTgy1gd2v5xofmoj31iv0u0n7a.jpg" style="zoom:200%;" />

The practice of k8s deploy processing

Link: [https://yeliansong.github.io/2020/03/22/Understand-The-K8S-Architecture/](https://yeliansong.github.io/2020/03/22/Understand-The-K8S-Architecture/)

### 1.2 The Concept Of K8S Objects

- Pod:  it's the atomic unit on the k8s platform. A pod contains different application containers which are relatively tightly coupled.

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdzxrzvnk5j30uo0ce0vo.jpg" style="zoom:200%;" />

- Node:  A pod always runs on a Node, a Node is a worker machine in k8s and may be either a virtual or a physical machine, depending on the cluster. Each Node is managed by the Master.

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdzxrxe66rj30uk0muaeg.jpg" style="zoom:200%;" />

  

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge0g4t2ilsj313e0ekmyt.jpg" style="zoom:200%;" />

- Cluster:  A set of Node machine, a cluster contains a worker Node and a master Node.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge4lcbalshj30rw0kagq8.jpg" style="zoom:200%;" />

## 2.  Create K8S Env With Kubeadm

We have 2 ways to create the K8S env. 1) make use of the Cloud including GCP, AWS or Huawei Cloud. They already have installed the K8S plugins. We can easily deploy our applications. 2) Create k8s env in the physical machines with the k8s tools. 

Link: [https://yeliansong.github.io/2020/03/14/kubeadm-concept-and-practice/](https://yeliansong.github.io/2020/03/14/kubeadm-concept-and-practice/)

## 3.  Ways To Deploy The K8S Objects

Generally there are 2 ways to deploy our application. Command and Yaml file.

- Command.

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge0gvhbutaj313g0sawi8.jpg" style="zoom:200%;" />

  

- YAML File

  Yaml is a type of configure file. The format is key-value. We also can deploy our applications with the YAML file. 

  >```yaml
  >apiVersion: apps/v1
  >kind: Deployment
  >metadata:
  >  name: nginx-deploymnet
  >spec:
  >  replicas: 3
  >  selector:
  >    matchLabels:
  >      app: web_server
  >  template: 
  >    metadata: 
  >      labels: 
  >        app: web_server
  >    spec: 
  >      containers:
  >      - name: nginx 
  >        image: nginx:1.7.9
  >```

Link: https://yeliansong.github.io/2020/04/08/How-to-write-the-YAML/ (How to Write the YAML)

## 4.  Workloads

### 4.1 Pods

Link: [https://kubernetes.io/zh/docs/concepts/workloads/pods/pod-overview/](https://kubernetes.io/zh/docs/concepts/workloads/pods/pod-overview/)

### 4.2 Controller

Link:  [https://kubernetes.io/zh/docs/concepts/workloads/controllers/replicaset/](https://kubernetes.io/zh/docs/concepts/workloads/controllers/replicaset/)

- Deployment

  The rules and format. (Show in the GCP)

  The relationship between Deployment  and Pod. (Show in the GCP) 

- DemonSet 

- ReplicationController

- ReplicaSet

  A ReplicaSet ensures that a specified number of pods replicas are running at any given time. But deployment is a high-level concept that manages ReplicaSets to Pods along with a lot of other useful features. Recommend using Deployments instead of directly using RS.

- StatefulSet

- Job



Link: [https://yeliansong.github.io/2020/04/25/Deployment/](https://yeliansong.github.io/2020/04/25/Deployment/)

PDF: [https://github.com/yeliansong/yeliansong.github.io/blob/master/_posts/Deployment.pdf](https://github.com/yeliansong/yeliansong.github.io/blob/master/_posts/Deployment.pdf)

## 5. K8S Network

Link: [https://yeliansong.github.io/2020/04/23/K8S-Network/](https://yeliansong.github.io/2020/04/23/K8S-Network/)

PDF: [https://github.com/yeliansong/yeliansong.github.io/blob/master/_posts/K8S%20Network.pdf](https://github.com/yeliansong/yeliansong.github.io/blob/master/_posts/K8S Network.pdf)

## 6. Deployment Strategy

Link: [https://yeliansong.github.io/2020/04/22/K8S-Deployment-Strategies/](https://yeliansong.github.io/2020/04/22/K8S-Deployment-Strategies/)

PDF:  [https://github.com/yeliansong/yeliansong.github.io/blob/master/_posts/K8S%20Deployment%20Strategies.pdf](https://github.com/yeliansong/yeliansong.github.io/blob/master/_posts/K8S Deployment Strategies.pdf)

## 7. Health Check

Link: [https://yeliansong.github.io/2020/04/11/Health-Check/](https://yeliansong.github.io/2020/04/11/Health-Check/)

PDF: [https://github.com/yeliansong/yeliansong.github.io/blob/master/_posts/Health%20Check.pdf](https://github.com/yeliansong/yeliansong.github.io/blob/master/_posts/Health Check.pdf)

## 8. Volume	

Link: [https://yeliansong.github.io/2020/04/14/Volume/](https://yeliansong.github.io/2020/04/14/Volume/)

PDF: [https://github.com/yeliansong/yeliansong.github.io/blob/master/_posts/Volume.pdf](https://github.com/yeliansong/yeliansong.github.io/blob/master/_posts/Volume.pdf)





# Part 3

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge44zgl16fj311k0qiqef.jpg" style="zoom:200%;" />












