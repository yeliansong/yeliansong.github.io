# K8S部署策略


### 1. 背景

我们总是将最终版本的应用程序部署到生产环境。 有多种方法可以保证发布生产的稳定和安全。 以下部分是 k8s 部署策略。

### 2. 策略

有 4 种方法可以进行生产发布。 1）滚动更新。 2）重新创建。 3) 蓝色/绿色。 4）金丝雀。 以下是详细信息。

- **重新创建更新**

   这是一种非常笨拙的更新方式。 销毁V1应用程序然后创建V2应用程序。 在一段时间内会遇到服务中断问题。

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2p8fwyufj31ga0e8wiv.jpg" style="zoom:200%;" />

- **滚动更新。**

   这是最常用的。

   - **使用 RC 执行自动滚动更新**

     >```yaml
     >apiVersion: v1
     >kind: ReplicationController
     >metadata:
     >name: kubia-v1
     >spec:
     >replicas: 3
     >template:
     >metadata:
     > name: kubia
     > labels:
     >   app: kubia
     >spec:
     > containers:
     >     - image: luksa/kubia:v1
     >       name: nodejs
     >---
     >apiVersion: v1
     >kind: Service
     >metadata:
     > name: kubia
     >spec:
     > type: NodePort
     > selector:
     >   app: kubia
     > ports:
     > - port: 80
     >   targetPort: 8080
     >   nodePort: 30007
     >```

     要运行此应用程序，将创建 ReplicationController 和 NodePort 服务，以便能够从外部访问该应用程序。 然后再打开另一个终端来监控服务。

     <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2n0jmlvwj31dq09yq59.jpg" style="zoom:200%;" />

     然后使用 kubectl 执行滚动更新，将创建应用程序的版本 2。 执行以下命令：

     >```外壳
     >kubectl 滚动更新 kubia-v1 kubia-v2 --image=luksa/kubia:v2
     >```

     <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2mlnx3v7j31dq07eq53.jpg" style="zoom:200%;" />

     <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2mmck3x8j31dk06y75x.jpg" style="zoom:200%;" />

     <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2mnx7txzj31160j20vd.jpg" style="zoom:200%;" />

     <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2mq854t1j31ce0tqgz2.jpg" style="zoom:200%;" />

     <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2n3378duj31eu0dqdix.jpg" style="zoom:200%;" />

   - **使用部署以声明方式更新应用程序**

     部署是一种高级资源，用于部署应用程序并以声明方式更新它们，而不是通过 RC 或 RS 来完成，这两者都被认为是较低级别的概念。

     <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2n83ztwtj30mq050t8z.jpg" style="zoom:200%;" />

     >```yaml
     >apiVersion: apps/v1
     >kind: Deployment
     >metadata:
     >name: kubia-v1
     >spec:
     >replicas: 3
     >selector:
     >matchLabels:
     > app: kubia
     >template:
     >metadata:
     > name: kubia
     > labels:
     >   app: kubia
     >spec:
     > containers:
     >     - image: luksa/kubia:v1
     >       name: nodejs
     >---
     >apiVersion: v1
     >kind: Service
     >metadata:
     > name: kubia
     >spec:
     > type: NodePort
     > selector:
     >   app: kubia
     > ports:
     > - port: 80
     >```

     同样要运行此应用程序，完成后，将 v1 部署容器更改为 v2，然后使用新版本进行部署。

     >```外壳
     >kubectl apply -f kubia-deploy-v2.yaml
     >```

     之后，您可以注意到将保留V1 RS。 所以版本从V2回滚到V1是非常容易的。

     <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2oder9xjj316203qab6.jpg" style="zoom:200%;" />

     <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2oeo5z3zj30u00ud47r.jpg" style="zoom:200%;" />

     使用此命令回滚部署。

     >```外壳
     >kubectl 推出撤消部署 kubia
     >```
     >
     >```外壳
     >kubectl 推出历史部署 kubia
     >```
     >
     >```外壳
     >kubectl 推出撤消部署 kubia --to-revision=1
     >```

     <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2ol1uaivj313c0b0gmr.jpg" style="zoom:200%;" />

- **蓝绿**

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2omtr0qij313i0iidl9.jpg" style="zoom:200%;" />

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2ouuod2xj31go0e8436.jpg" style="zoom:200%;" />

   实际上这个部署需要V1和V2应用程序已经存在。 客户端通过标签连接Deployment。

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2otd304pj312u0iedn4.jpg" style="缩放:200%;" />
   
   - **金丝雀部署**
   
      <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2p1g1r2sj312g0iqjwu.jpg" style="zoom:200%;" />
   
   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2p1vzi0nj312i0i679j.jpg" style="zoom:200%;" />
   
   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2p2ln3wcj31h00e6dkh.jpg" style="zoom:200%;" />
