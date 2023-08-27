# 了解K8S架构


### 1.k8s组件架构。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images00831rSTgy1gd2v5xofmoj31iv0u0n7a.jpg" style="zoom:200%;" />

好吧，这很容易理解。 如上所述，主节点是最重要的。 它控制其他节点加入集群。 API服务器也暴露在外。 通过主节点，即可安排其他节点。

### 2.实例操练

#### 目标：创建k8s集群，然后将应用程序部署到这2个节点。

#### 步骤：

- 使用kubeadm init创建主k8s集群，然后将node1和node2加入集群。

- 在主节点中，部署应用程序，复制数为2。

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images00831rSTgy1gd2wbfwqq3j31fe0460u9.jpg" style="zoom:200%;" />

- 执行后，部署完成。 您可以执行命令“kubectl get pods”，显示部署情况。

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images00831rSTgy1gd2wc6ysd1j321c044q4u.jpg" style="zoom:200%;" />

   该应用程序分别部署在2个节点中。

### 3.了解流程

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images00831rSTgy1gd2vq6vm42j313s0u01co.jpg" style="zoom:200%;" />

这就是整个过程。

当执行“kubectl run”时，会调用API Server，然后API Server通知Controller Server创建部署资源。 之后Schedule服务会将任务安排到node1和node2上。 在node1和node2中，kubelet会根据任务创建pod。 Kube-proxy 将为这 2 个节点安排网络配置。
