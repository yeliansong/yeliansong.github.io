# Volume


### 1.emptyDir

这是卷的基础。 生命周期取决于Pod。 当相关 Pod 被删除时，该卷也会被删除。 所以我们可以将其视为Pod的路径。 Pod 的所有容器共享这个 voiume。 让我们展示如何设置音量配置。

>```yaml
>apiVersion: v1
>kind: Pod
>metadata:
>name: producer-consumer
>spec:
>containers:
> - image: busybox
>   name: producer
>   volumeMounts:
>   - mountPath: /producer_dir
>     name: shared-volume
>   args:
>   - /bin/sh
>   - -c
>   - echo "hello world" > /producer_dir/hello; sleep 30000
>
> - image: busybox
>   name: consumer
>   volumeMounts:
>   - mountPath: /consumer_dir
>     name: shared-volume
>   args:
>   - /bin/sh
>   - -c
>   - cat /consumer_dir/hello; sleep 30000
>
> volumes:
> - name: shared-volume
>   emptyDir: {}
>```

上面的文件是关于配置卷的练习。 我们在pod中设计了两个容器，一个是生产者，将日志写入路径文件中，另一个是消费者，从文件中读取日志。 很容易理解，这两个容器共享 Pod 的存储。

### 2. 主机路径

这种体积很少使用。 这并不常见。 这用于 Docker 主机挂载 Pod 的现有路径。 所以Pod和容器有很强的耦合性。 但如果 pod 被删除，该卷仍然存在。 但是，请避免使用此类卷。

### 3. 外部存储提供商

这使用外部存储提供者来实现卷。 例如使用AWS，GCE或Azure等。 让我展示一下配置。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdrv241tr4j31180s2tza.jpg" style="zoom:200%;" />

这使用了 aws 存储。 使用它的优点是使 k8s 集群和卷隔离。 k8s集群销毁时没有影响。

### 4.持久卷和持久卷声明

从第 3 节中，我们知道我们可以使用 k8s 卷的外部存储。 但有一个问题，实际上存储系统总是用于管理的，而k8s部署是用于开发人员的。 有不同的部门。 如何平衡差距。 解决方法是PV和PVC。

PV由管理部门维护，是安排的外部存储。 但PVC是给开发商用的。 部署微服务时，可以设置pvc来安排PV的空间。 因此PV和PVC协调部署整个系统。

#### 4.1 NFS 持久卷

首先，在主从节点上安装NFS服务。 还定义安装路径。 以下是 PV 和 PVC 配置文件。

>```yaml
>nfs-pv.yaml
>apiVersion: v1
>kind: PersistentVolume
>metadata:
>name: mypv1
>spec:
>capacity:
>storage: 1Gi
>accessModes:
>   - ReadWriteOnce
> persistentVolumeReclaimPolicy: Recycle
> storageClassName: nfs
> nfs:
>   path: /tmp/pv1
>   server: 10.128.0.2
>```

>```yaml
>nfs-pvc.yaml
>apiVersion: v1
>kind: PersistentVolumeClaim
>metadata:
>name: mypvc1
>spec:
>accessModes:
>   - ReadWriteOnce
> resources:
>   requests:
>     storage: 1Gi
> storageClassName: nfs
>```

>```yaml
>pod.yaml
>apiVersion: v1
>kind: Pod
>metadata:
>name: mypod1
>spec:
>containers:
>   - name: mypod1
>     image: busybox
>     args:
>     - /bin/sh
>     - -c
>     - sleep 30000
>     volumeMounts:
>     - mountPath: "/mydata"
>       name: mydata
> volumes:
>   - name: mydata
>     persistentVolumeClaim:
>       claimName: mypvc1
>```

在PV YAML文件中，我们可以定义持久卷策略类型。 有**保留**、**回收**、**删除**三种类型。默认策略是删除。

- **Retain**：用户删除了一个perpetitiveVolumeClaim，对应的perpetitiveVolume并没有被删除。 相反，它已进入发布阶段，可以手动恢复其所有数据。
- **Recycle**：与Retain不同，删除PVC后数据无法手动恢复。
- **删除**：这是默认模式。 意味着当用户删除相应的图片时，动态pv会自动删除。

运行 pod 时，将挂载 PVC 路径。 然后使用命令向挂载路径写入一些内容。 从下面的运行结果，我们可以了解NFS中的PV和PVC。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdski4591gj31n60ei1kx.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdskilgw5bj31es0bkndy.jpg" style="zoom:200%;" />

![](https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/7777.jpeg)

关于是静态规定，还有另一种规定，它是动态规定。 它根据情况安排存储。

#### 4.2 数据库实践

- 后台：使用NFS PV和PVC在节点关闭时进行数据库备份，以验证数据持久性。

- 步骤：

   - 根据以下配置文件部署PV和PVC。

     >```yaml
     >mysql-pvc.yaml
     >apiVersion: v1
     >kind: PersistentVolumeClaim
     >metadata:
     >name: mysql-pvc
     >spec:
     >accessModes:
     >   - ReadWriteOnce
     > resources:
     >   requests:
     >     storage: 1Gi
     > storageClassName: nfs



- > ```yaml
  > mysql-pv.yaml
  > apiVersion: v1
  > kind: PersistentVolume
  > metadata:
  > name: mysql-pv
  > spec:
  > accessModes:
  >    - ReadWriteOnce
  >  capacity:
  >    storage: 1Gi
  >  persistentVolumeReclaimPolicy: Retain
  >  storageClassName: nfs
  >  nfs:
  >    path: /tmp/mysql-pv
  >    server: 10.128.0.2	yaml
  > ```

- 部署 mysql pod 和服务

  - > ```yaml
    > piVersion: v1
    > kind: Service
    > metadata:
    > name: mysql
    > spec:
    > ports:
    >  - port: 3306
    >  selector:
    >    app: mysql
    > 
    > ---
    > apiVersion: apps/v1
    > kind: Deployment
    > metadata:
    >  name: mysql
    > spec:
    >  selector:
    >    matchLabels:
    >      app: mysql
    >  template:
    >    metadata:
    >      labels:
    >        app: mysql
    >    spec:
    >      containers:
    >      - image: mysql:5.6
    >        name: mysql
    >        env:
    >        - name: MYSQL_ROOT_PASSWORD
    >          value: password
    >        ports:
    >        - containerPort: 3306
    >          name: mysql
    >        volumeMounts:
    >        - name: mysql-persistent-storage
    >          mountPath: /var/lib/mysql
    >      volumes:
    >      - name: mysql-persistent-storage
    >        persistentVolumeClaim:
    >          claimName: mysql-pvc
    > ```

    

    - 使用客户端访问数据库，向数据库中插入一些消息。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdskym6x3zj31nu04o486.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdskz4v39sj312k0oo1kx.jpg" style="zoom:200%;" />

- 关闭node1，数据库会自动备份到node2。 备份完成后，我们可以在master节点进行验证

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdsl11wlkoj31ic08anb8.jpg" style="zoom:200%;" />

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gdsl1l4npzj31mm0ji7wh.jpg" style="zoom:200%;" />

  
