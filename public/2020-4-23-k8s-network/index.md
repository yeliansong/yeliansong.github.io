# K8S网络


K8S网络分为3级。 从内到外，有3种： **1）容器网络。 2) 集群内网络。 3) 外部集群网络。** 以下是详细信息，

### 1.容器网络

Docker 网络仅限于主机本身。 默认情况下，它创建一个名为 docker0 的虚拟网桥，并为每个容器分配一个附加到网桥 docker0 的虚拟乙烷。 因此，在 Docker 中，如果两个容器驻留在同一主机上，则它们可以相互通信。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge43fqcv1xj310e0m2q7z.jpg" style="zoom:200%;" />

### 2. 集群内网络

这意味着 Pod 之间进行通信。 集群中所有Pod共享同一个网段。 所以 Pod 之间可以直接通信。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge438gf6o3j311y0gejxe.jpg" style="zoom:200%;" />

也可以将Pod暴露给一个服务，然后集群中的其他应用程序就可以访问该Pod服务。 像这样，

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge43aap8l7j30u00w3wm2.jpg" style="zoom:200%;" />



### 3.外部集群网络

如何从外部访问k8s集群网络？ 构建网络模型有3种方法。

#### 3.1。 负载均衡器

LoadBalacer 服务是向互联网公开服务的标准方法。 但只有在AWS或Google Cloud上才能使用此功能。 在 GKE 上，这将启动一个网络负载均衡器，该负载均衡器将为您提供一个 IP 地址，将所有流量转发到您的服务。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge3xk6fpu4j30u00x6dnd.jpg" style="zoom:200%;" />

如果你想直接公开一个服务，这是默认方法。 您指定的端口上的所有流量都将转发到该服务。没有过滤、没有路由等。这意味着您可以向其发送几乎任何类型的流量，例如 HTTP、TCP、UDP。 Websocket、gRPC 或其他。

最大的缺点是，您使用 LoadBalancer 公开的每个服务都将获得自己的 IP 地址，并且您必须为每个公开的服务支付 LoadBalancer 费用，这可能会很昂贵。

#### 3.2。 节点端口

NodePort 服务是将外部流量直接发送到您的服务的最原始方式。 NodePort，顾名思义，在所有Node上打开一个特定的端口，任何发送到该端口的流量都会转发到服务。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge3xha2c9xj30u00vpwqh.jpg" style="zoom:200%;" />

#### 3.3。 入口

与上述所有示例不同，Ingress 实际上不是一种服务。 相反，它位于多个服务的前面，并充当集群的“智能路由器”或入口点。您可以使用 Ingress 执行许多不同的操作，并且有许多类型的 Ingress 控制器具有不同的功能。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge3xshdrdlj31080mg441.jpg" style="zoom:200%;" />

>```yaml
>apiVersion: extensions/v1beta1
>kind: Ingress
>metadata:
>name: my-ingress
>spec:
>backend:
>serviceName: other
>servicePort: 8080
>rules:
> - host: foo.mydomain.com
>   http:
>     paths:
>     - backend:
>         serviceName: foo
>         servicePort: 8080
> - host: mydomain.com
>   http:
>     paths:
>     - path: /bar/*
>       backend:
>         serviceName: bar
>         servicePort: 8080
>```
