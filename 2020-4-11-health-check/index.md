# 健康检查


### 1.关于K8S健康检查

健康检查是k8s编排的重要功能。 K8s 可以监控这些容器，并在发生故障时自动重新启动它们。 如果容器的主进程崩溃，k8s将重新启动容器。 另外，如果你的应用程序有bug导致它偶尔崩溃，k8s会自动重新启动它。健康检查有两种方式。 活跃度和准备度。 有什么不同？ 以及如何使用这些？

- **活性探针**

   k8s 可以通过活性探针检查容器是否仍然存活。 您可以在 pod 规范中为每个容器指定一个活性探针。 k8s会定期执行探测，如果探测失败则重启容器。

   活性健康检查配置文件。
   
   - > ```yaml
     > apiVersion: v1
     > kind: Pod
     > metadata:
     > labels:
     > test: liveness
     > name: liveness
     > spec:
     > restartPolicy: OnFailure
     > containers:
     >  - name: liveness
     >    image: busybox
     >    args:
     >    - /bin/sh
     >    - -c
     >    - touch /tmp/healthy; sleep 30; rm -rf /tmp/healthy; sleep 60
     >    livenessProbe:
     >      exec:
     >        command:
     >        - cat
     >        - /tmp/healthy
     >      initialDelaySeconds: 10
     >      periodSeconds: 5
     > ```

从这个配置文件中，我们定义了 livenessProbe。 每 5 秒，探测器就会检测并执行该命令。 如果失败，将再次重新启动 pod。

- 准备状况健康检查配置文件。

  - > ```yaml
    > apiVersion: v1
    > kind: Pod
    > metadata:
    > labels:
    > test: readiness
    > name: readiness
    > spec:
    > restartPolicy: OnFailure
    > containers:
    >  - name: readiness
    >    image: busybox
    >    args:
    >    - /bin/sh
    >    - -c
    >    - touch /tmp/healthy; sleep 30; rm -rf /tmp/healthy; sleep 60
    >    readinessProbe:
    >      exec:
    >        command:
    >        - cat
    >        - /tmp/healthy
    >      initialDelaySeconds: 10
    >      periodSeconds: 5
    > ```

  该文件类似于liveness。 刚刚更改了键值。 对于这一点，当失败时，会重新启动 pod 一次，之后，设置 readiness 就没有用了。

  ### 2.滚动更新中的健康检查实践

  健康检查如何运用在滚动更新中？ 想象一种情况，你将应用程序从V1更新到V2，但实际上V2应用程序是错误的，你没有使用检查方法来验证这一点。 你将如何解决这个问题？ 我们可以使用健康检查。

  - 首先，使用 v1 部署 10 个副本。

    >```yaml
    >apiVersion: apps/v1
    >kind: Deployment
    >metadata:
    >name: app
    >spec:
    >replicas: 10
    >selector:
    >matchLabels:
    > run: app
    >template:
    >metadata:
    > labels:
    >   run: app
    >spec:
    > containers:
    >     - name: app
    >       image: busybox
    >       args:
    >       - /bin/sh
    >       - -c
    >       - sleep 10; touch /tmp/healthy; sleep 30000
    >       readinessProbe:
    >         exec:
    >           command:
    >           - cat
    >           - /tmp/healthy
    >         initialDelaySeconds: 10
    >         periodSeconds: 5
    >```

    <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images007S8ZIlgy1gdpzbx6r8oj318i0qm7wh.jpg" style="zoom:200%;" />

- 然后滚动更新错误的应用程序。 它将触发探测器进行检测。

   >```yaml
   >apiVersion: apps/v1
   >kind: Deployment
   >metadata:
   >name: app
   >spec:
   >replicas: 10
   >selector:
   >matchLabels:
   > run: app
   >template:
   >metadata:
   > labels:
   >   run: app
   >spec:
   > containers:
   >     - name: app
   >       image: busybox
   >       args:
   >       - /bin/sh
   >       - -c
   >       - sleep 3000
   >       readinessProbe:
   >         exec:
   >           command:
   >           - cat
   >           - /tmp/healthy
   >         initialDelaySeconds: 10
   >         periodSeconds: 5
   >```

 使用此配置文件部署时，会失败。 下面是结果。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images007S8ZIlgy1gdpzk08tjbj313i0qe4qp.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images007S8ZIlgy1gdpztqjufbj30qa0zqx47.jpg" style="zoom:200%;" />

从结果中我们可以看到新的复制无法通过健康检查。 但健康检查仍然是最古老的复制。 这是因为 maxSurge 和 maxUnavailable。 如果文件中没有定义，则使用默认值。maxSurge 和 maxUnavailable 用于定义滚动更新副本和故障副本。

### 3.滚动更新

此部分不用于健康检查。 只是之前学习的总结。 本节包括滚动更新和回滚。 滚动更新非常简单，只需运行命令，就会自动部署更改。 我们主要讨论回滚。

当您进行滚动更新时，您可以记录修订版本。 当您想要回滚时，可以定位到该版本。

- Kuebctl apply -f rollback.yaml --record

   当添加记录参数时，会记录回溯。

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images00831rSTgy1gdp45c5s14j31ig0oohdt.jpg" style="zoom:200%;" />

- Kubectl 推出历史部署 http

   这将显示所有部署历史版本。

   <img src="https://p.ipic.vip/zttryj.jpg" alt="55555" style="zoom:200%;" />

- Kubectl 推出撤消部署 http --to-revision=1

   这将推出该版本。

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images00831rSTgy1gdp46orwccj31mw0aa4gs.jpg" style="zoom:200%;" />

   此外，当您成功推出后，版本将随着您的部署而更改。

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images00831rSTgy1gdp47k5pepj31760bo170.jpg" style="zoom:200%;" />
