# 云技术、容器及K8S 分享


# 第一部分：

这部分内容包括云历史、容器技术、k8s等基础知识。

## 1. 云技术

### 1.1 云计算的历史

 [https://skyao.io/learning-cloudnative/introduction/history.html]()

- IaaS：基础设施即服务

- PaaS：平台即服务

- SaaS：软件即服务

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdyavrtx33j315t0u0ndg.jpg" style="zoom:200%;" />

### 1.2 云原生

 [https://skyao.io/learning-cloudnative/introduction/background.html](https://skyao.io/learning-cloudnative/introduction/background.html)

### 1.3 DevOps 和优势

 [https://www.qikegu.com/docs/4262](https://www.qikegu.com/docs/4262)

 [https://skyao.io/learning-cloudnative/devops/](https://skyao.io/learning-cloudnative/devops/)

## 2. 容器技术

#### 2.1 虚拟化技术

虚拟化是指创建某种事物的虚拟版本的行为，包括虚拟计算机硬件平台、存储设备和计算机网络资源等。它让您使用传统上与硬件绑定的资源创建有用的IT服务，允许您使用物理资源 通过将其功能分配给许多用户或环境来充分发挥机器的能力。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdyyrcui4pj30vi072abp.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdyys2rfejj315007ugn1.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdyyz7cw72j30t20cg0ul.jpg" style="zoom:200%;" />

### 2.2 虚拟机与容器

- **VM：虚拟机**

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdyz7hbm2aj31380mstb7.jpg" style="zoom:200%;" />

- **容器**

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdyzobodq1j312a0jakjl.jpg" style="zoom:200%;" />



<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdyzsk2mhrj30wi0ieaca.jpg" style="zoom:200%;" />

容器与虚拟机的比较

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdz2fu0w9jj313w0ni0vh.jpg" style="zoom:200%;" />

 **使用Container的优点：**

- 容器更加轻量级，它类似于在主机操作系统中运行的单个隔离进程。
- 容器启动比虚拟机更快。
- 容器更适合微服务。

### 2.3 码头工人

Docker是一家位于旧金山的基于容器技术的初创公司。 这是容器技术的最佳实践。 然后它就成为与其他企业竞争的标准。 Docker代表容器技术。

## 3. 微服务

### 3.1 单一应用程序

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdz9039dlmj30f80lajsx.jpg" style="zoom:100%;" />

单体应用程序是传统的部署设计模型。 参考上图，进程数是相互依赖的。 缺点也是显而易见的，整个系统的部署比较繁琐。 升级单个应用程序是有风险的。 因为它与其他部分相连。 另外，开发人员和运维工作很难分开，开发人员有时需要关心管理的问题，系统运维人员也需要定位是否是软件问题。

### 3.2 微服务

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdzaf61qs1j31e40s2qj8.jpg" style="zoom:200%;" />

  上图非常形象的表达了微服务的范围。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdzas1nrvjj30zc0fk767.jpg" style="zoom:200%;" />

从单体应用到微服务应用。

微服务是一种软件开发技术，它将应用程序安排为松散耦合服务的集合。 在微服务架构中，服务是细粒度的，协议是轻量级的。

- 更容易构建和维护应用程序。
- 使用技术的灵活性和可扩展性
- 与 Jenkins 等持续集成工具轻松集成和自动部署。 还可以实现持续交付。
——提高开发效率。 降低不同团队之间的沟通成本。
- 不同服务的代码可以用不同的语言编写。 打破不同语言和技术的障碍。

## 4. 库伯内特斯

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdzc0dus8ej31cj0u07wj.jpg" style="zoom:200%;" />



[https://www.infoq.cn/article/U2a_7ekuvhmb7dSNp27V](https://www.infoq.cn/article/U2a_7ekuvhmb7dSNp27V)



# 第二部分：

这部分是k8s的细节。 会介绍k8s的要点和一些做法。

## 1. K8S 开胃菜

### 1.1 了解K8S集群架构

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdzgd32o49j314c0f40ub.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdzgem5svuj312y0fu41d.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/00831rSTgy1gd2v5xofmoj31iv0u0n7a.jpg" style="zoom:200%;" />

k8s部署处理的实践

链接：[https://yeliansong.github.io/2020/03/22/Understand-The-K8S-Architecture/](https://yeliansong.github.io/2020/03/22/Understand-The-K8S -建筑学/）

### 1.2 K8S对象的概念

- Pod：是k8s平台上的原子单元。 一个 Pod 包含不同的应用程序容器，这些容器耦合得相对紧密。

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdzxrzvnk5j30uo0ce0vo.jpg" style="zoom:200%;" />

- Node：Pod 总是运行在 Node 上，Node 是 k8s 中的工作机器，可以是虚拟机也可以是物理机，具体取决于集群。 每个Node都由Master管理。

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdzxrxe66rj30uk0muaeg.jpg" style="zoom:200%;" />

  

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge0g4t2ilsj313e0ekmyt.jpg" style="zoom:200%;" />

- 集群：一组Node机器，一个集群包含一个worker Node和一个master Node。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge4lcbalshj30rw0kagq8.jpg" style="zoom:200%;" />

## 2. 使用 Kubeadm 创建 K8S 环境

我们有两种创建 K8S 环境的方法。 1）利用云，包括GCP、AWS或华为云。 他们已经安装了 K8S 插件。 我们可以轻松部署我们的应用程序。 2）使用k8s工具在物理机中创建k8s环境。

链接：[https://yeliansong.github.io/2020/03/14/kubeadm-concept-and-practice/](https://yeliansong.github.io/2020/03/14/kubeadm-concept-and -实践/）

## 3. K8S 对象的部署方式

通常有两种方法来部署我们的应用程序。 命令和 Yaml 文件。

- 命令。

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge0gvhbutaj313g0sawi8.jpg" style="zoom:200%;" />

  

- YAML 文件

   Yaml 是一种配置文件。 格式为键值对。 我们还可以使用 YAML 文件部署我们的应用程序。

   >```yaml
   >apiVersion: apps/v1
   >kind: Deployment
   >metadata:
   >name: nginx-deploymnet
   >spec:
   >replicas: 3
   >selector:
   >matchLabels:
   > app: web_server
   >template: 
   >metadata: 
   > labels: 
   >   app: web_server
   >spec: 
   > containers:
   >     - name: nginx 
   >       image: nginx:1.7.9
   >```

链接：https://yeliansong.github.io/2020/04/08/How-to-write-the-YAML/（如何编写YAML）

## 4. 工作负载

### 4.1 Pod

链接：[https://kubernetes.io/zh/docs/concepts/workloads/pods/pod-overview/](https://kubernetes.io/zh/docs/concepts/workloads/pods/pod-overview/)

### 4.2 控制器

链接：[https://kubernetes.io/zh/docs/concepts/workloads/controllers/replicaset/](https://kubernetes.io/zh/docs/concepts/workloads/controllers/replicaset/)

- 部署

   规则和格式。 （在 GCP 中显示）

   Deployment 和 Pod 之间的关系。 （在 GCP 中显示）

- DemonSet 

- ReplicationController

- ReplicaSet

   ReplicaSet 可确保在任何给定时间运行指定数量的 pod 副本。 但部署是一个高级概念，它管理 Pod 的 ReplicaSet 以及许多其他有用的功能。 推荐使用 Deployments 而不是直接使用 RS。

- 状态集

- 工作



链接：[https://yeliansong.github.io/2020/04/25/Deployment/](https://yeliansong.github.io/2020/04/25/Deployment/)

PDF：[https://github.com/yeliansong/yeliansong.github.io/blob/master/_posts/Deployment.pdf](https://github.com/yeliansong/yeliansong.github.io/blob/master/ _posts/部署.pdf）

## 5.K8S网络

链接：[https://yeliansong.github.io/2020/04/23/K8S-Network/](https://yeliansong.github.io/2020/04/23/K8S-Network/)

PDF：[https://github.com/yeliansong/yeliansong.github.io/blob/master/_posts/K8S%20Network.pdf](https://github.com/yeliansong/yeliansong.github.io/blob/ master/_posts/K8S Network.pdf)

## 6. 部署策略

链接：[https://yeliansong.github.io/2020/04/22/K8S-Deployment-Strategies/](https://yeliansong.github.io/2020/04/22/K8S-Deployment-Strategies/)

PDF：[https://github.com/yeliansong/yeliansong.github.io/blob/master/_posts/K8S%20Deployment%20Strategies.pdf](https://github.com/yeliansong/yeliansong.github.io/ blob/master/_posts/K8S 部署策略.pdf)

## 7. 健康检查

链接：[https://yeliansong.github.io/2020/04/11/Health-Check/](https://yeliansong.github.io/2020/04/11/Health-查看/）

PDF：[https://github.com/yeliansong/yeliansong.github.io/blob/master/_posts/Health%20Check.pdf](https://github.com/yeliansong/yeliansong.github.io/blob/ master/_posts/健康检查.pdf)

## 8. volume

链接：[https://yeliansong.github.io/2020/04/14/Volume/](https://yeliansong.github.io/2020/04/14/Volume/)

PDF：[https://github.com/yeliansong/yeliansong.github.io/blob/master/_posts/Volume.pdf](https://github.com/yeliansong/yeliansong.github.io/blob/master/ _posts/Volume.pdf)





# 第 三部分

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge44zgl16fj311k0qiqef.jpg" style="zoom:200%;" />
