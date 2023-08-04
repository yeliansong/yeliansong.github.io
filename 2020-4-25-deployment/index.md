# K8S部署


Deployment 为 Pod 和 ReplicaSet 提供声明性更新。 我们可以利用许多部署功能。

本章涵盖**更新部署**、**回滚部署**、**调用部署**、**暂停和恢复部署**和**部署状态**。

首先，我们创建一个部署。

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

- **更新部署**

   参考此链接：[https://yeliansong.github.io/2020/04/22/K8S-Deployment-Strategies/](https://yeliansong.github.io/2020/04/22/K8S-Deployment- 策略/）

   它涵盖了部署的推出和回滚。

- **缩放部署**

   您可以根据需要使用以下命令来扩展 Deployment。

   >```外壳
   >kubectl scale deployment nginx-deploymnet --replicas=10
   >```

   假设集群中启用了水平 Pod 自动缩放，您可以为 Deployment 设置自动缩放器，并根据现有 Pod 的 CPU 利用率选择要运行的最小和最大 Pod 数量。

   >```外壳
   >kubectl autoscale deployment nginx-deploymnet --min=10 --max=15 --cpu-percent=20
   >```

- **暂停和恢复部署**
   您可以在触发一个或多个更新之前暂停部署，然后再恢复它。 这允许您在暂停和恢复之间应用多个修复，而不会触发不必要的推出。

   >```外壳
   >kubectl rollout pause deployment nginx-deploymnet
   >```

   这将暂停部署，然后您可以修补此部署的更改。

   >```
   >kubectl set image deployment nginx-deploymnet nginx=nginx:1.16.1
   >```

   之后，您可以恢复部署。

   >```外壳
   >kubectl rollout resume deployment nginx-deploymnet
   >```

- **部署状态**

   Deployment 在其生命周期中会进入各种状态。 它可以是正在进展、已完成或未进展。

   当执行以下任务之一时，部署进入进度状态。

   - Deployment 创建一个新的 ReplicaSet
   - Deployment 正在扩展其最新的 ReplicaSet
   - Deployment 正在缩减其旧的 ReplicaSet
   - 新 Pod 已准备就绪或可用

   您可以使用 kubectl rollout status 来监控进度。

   当具有以下特征时输入完整。

   - 所有副本均已更新至您指定的最新版本。
   - 所有副本均可用
   - 部署的旧副本没有正在运行。

   匹配失败的原因有以下一项。

   - 配额不足
   - 就绪探针故障
   - 图像拉取错误
   - 权限不足
   - 限制范围
   - 应用程序运行时配置错误

   以下命令使用progressDeadlineSeconds 设置规范，以使控制器在您定义的时间之后报告部署缺乏进度。

   >```外壳
   >Kubectl patch deployment nginx-deployment -p '{"spec":{"progressDeadlineSeconds":600}}'
   >```
