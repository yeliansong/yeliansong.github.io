# 如何编写 YAML


### 1.如何编写YAML

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

好的，让我们分析一下这个 YAML 示例。
它使用缩进来表示图层。 每一层都是相互依赖、相互调用的。每个key的含义。

apiVersion：这是当前配置版本。

Kind：创建的资源类型。

元数据：资源元数据。

规格：部署的规格。

选择器：用于选择哪个模板。

模板：定义Pod信息。

所以，由此，我想我可以用思维导图来描述。我们可以参考下面。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images00831rSTgy1gdjavs7f3cj316b0u043t.jpg" style="zoom:200%;" />

### 2. 如何编写作业配置文件

首先，我们需要确定工作的目标。 容器可以分为两种，一种是为服务器持久化运行，另一种是只运行一项作业，一次运行。 这就是工作。 如何定义作业配置文件。

>```yaml
>apiVersion: batch/v1
>kind: Job
>metadata:
>name: myjob
>spec:
>parallelism: 3
>template:
>metadata:
> name: myJob 
>spec: 
> containers:
>     - name: hello 
>       image: busybox
>       command: ["echo", "hello k8s job" ]
>     restartPolicy: OnFailure
>```

实际上作业配置有很多种，包括常规作业、并行作业和定时作业。 还需要灵活使用restartPolicy参数。 OnFailure 表示失败时，将重新启动 pod。 您也可以设置“never”，这意味着将重新启动 pod，直到成功为止。

### 3. YAML 总结

最后，我认为如果掌握了规则，YAML并不难。 它由层组成。 因此，如果您了解每一层，您就可以设计您的部署、作业或服务。
