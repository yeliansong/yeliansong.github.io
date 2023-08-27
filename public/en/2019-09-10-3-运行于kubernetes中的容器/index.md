# 三、Containers running in Kubernetes


### 1. Why create a POD

We know that POD is the smallest unit managed by Kubernetes. Why does Kubernetes not directly manage containers, but manage PODs? There is a reason for this. We know that a container is a single process. What does it mean? The design idea of a container is that each container only runs one process. If you use dry bernetes to directly manage these containers, it must be complicated, so I will do it The POD is introduced to realize resource and network isolation between containers. All containers under the same POD share network and system resources. However, all containers in a POD must be a whole that is closely integrated with logical services. They There must be a strong connection. Each container can be distinguished by port.



### 2. How to plan the containers in the POD

As I just said, a group of containers are placed in a POD. How to plan these containers? Is it possible to put all the containers in the project into a POD? Because POD is relatively lightweight, it is encouraged to use as many PODs as possible. When planning the containers in POD, you need to consider whether the business logic of your group of containers is closely connected, and whether you want to scale your containers. , these are your judgment conditions.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6ur9w2djtj30fc087n06.jpg" style="zoom:200%;" />



A good example is that the front-end and back-end are divided into two PODs for deployment.



### 3. YAML file analysis and POD creation

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6ur9wxdumj30by06p75b.jpg" style="zoom:200%;" />

Very EASY, in fact, a YAML file contains: kind, metadata, spe these things. metadata is used to define the data of POD, and spec is used to define all container data under this POD.

There are several commands to learn: Kubectl create -f a.yaml, this is to create the required POD through the yaml file. To obtain the log information of the specified container in the POD, you can use kubectl logs kula -c kubia. To obtain the yaml or json format file of the running POD, you can use kubectl get po kubia -o yaml or kubectl get po kubia -o json. kubectl port-forward kubela 8888:8080 is used for port mapping.



### 4. POD label

There is no doubt that the role of labels is to distinguish PODs. So adding tags is to better manage your POD. A POD can set multiple tags, and then use the tags to schedule PODs uniformly. Some commands of the label can be viewed through the manual, including modifying labels, setting labels, adding labels, and so on.



### 5. Namespace

Let’s figure out first, the purpose of creating a Namespace. We know that we already have the concept of labels, and labels can also be used for grouping, but why do we still need to create a Namespace? The grouping of tags is still incomplete. A POD can have multiple tags, so I think tags are still used more by O&M personnel. The Namespace is different. Each POD has only one Namespace. Grouping is more thorough.

Let's see how to play Namespace. kubectl get ns: List all namespaces, kubectl get po --namespace kube-system: List all PODs of the specified Namespace. kubectl create namespace custom-namespace, create a Namespace.
