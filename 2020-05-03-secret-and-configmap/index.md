# Secret And ConfigMap


### 1. 背景

到目前为止，也许您不必将任何类型的配置数据传递给应用程序。 因为几乎所有应用程序都需要配置，不应将其融入到构建的应用程序本身中。 本文介绍了将配置数据传递到应用程序的两种方法。

### 2.密钥

密钥是因为您传递给容器的信息是敏感的。 K8s 提供了一个单独的对象，称为 Secret。 有 4 种创建 Secret 的方法。

- 通过 --from-literal

   >```外壳
   >kubectl create secret generic mysecret --from-literal=username=admin --from-literal=password=123456
   >```

- 通过--from-file，每个文件包含一项。

   >```外壳
   >echo -n admin > ./username
   >echo -n 123456 > ./password
   >kubectl create secret generic mysecret1 --from-file=./username --from-file=./password 
   >```

- 通过--from-env-file。 在 env.txt 中，每一行键值都匹配一项。

   >```外壳
   >cat << EOF > env.txt
   >username=admin
   >password=123456
   >EOF
   >kubectl create secret generic mysecret --from-env-file=env.txt
   >```

- 通过 YAML 文件。

   >```外壳
   >apiVersion: v1
   >kind: Secret
   >metadata:
   >name: mysecret
   >data:
   >username: YWRtaW4=
   >password: NTY3ODk=
   >```

   用户名和密码是敏感信息，因此会被加密。 然后可以使用：“kubectl apply -f my Secret.yaml”来创建秘密。

   创建秘密后，可以使用命令显示秘密。 像这样。

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gef6b6hi5xj315c05wjsr.jpg" style="zoom:200%;" />

   您也可以使用describe命令来显示详细信息。

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gef6c7frckj317m0bygna.jpg" style="zoom:200%;" />

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gef6cxavpzj31d00hidjo.jpg" style="zoom:200%;" />

   在此图中，您可以看到密码和用户名已加密。

### 3.如何在Pod中使用secret

我们知道，Secret是k8s中分离的对象，所以pod会通过卷来使用secret。 如何使用，如下。

- 创建 pod，在 pod 中定义卷，也来自秘密。 （体积）

   >```外壳
   >apiVersion: v1
   >kind: Pod
   >metadata:
   >name: mypod
   >spec:
   >containers:
   > - name: mypod
   >   image: busybox
   >   args:
   >     - /bin/sh
   >     - -c
   >     - sleep 10; touch /tmp/healthy; sleep 30000
   >   volumeMounts:
   >   - name: foo
   >     mountPath: "/etc/foo"
   >     readOnly: true
   > volumes:
   > - name: foo
   >   secret:
   >     secretName: mysecret
   >```

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gef822d1fgj31du082q4e.jpg" style="zoom:200%;" />

   从Yaml文件中我们可以看到，将秘钥值挂载到路径：/etc/foo. 然后我们就可以查看秘密了。

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gef89v4uzoj30ny0mqwv9.jpg" style="zoom:200%;" />

 也可以将数据保存到组路径中。 这样，我们就可以保存秘密加密。

- 创建 Pod，在 Pod 中定义 env 变量。 （环境）

   >```外壳
   >apiVersion: v1
   >kind: Pod
   >metadata:
   >name: mypod-env
   >spec:
   >containers:
   > - name: mypod-env
   >   image: busybox
   >   args:
   >     - /bin/sh
   >     - -c
   >     - sleep 10; touch /tmp/healthy; sleep 30000
   >   env:
   >     - name: SECRET_USERNAME
   >       valueFrom:
   >         secretKeyRef:
   >           name: mysecret
   >           key: username
   >     - name: SECRET_PASSWORD
   >       valueFrom:
   >         secretKeyRef:
   >           name: mysecret
   >           key: password
   >```

   在 pod 中，定义键和值。 然后就可以通过环境变量获取值了。

### 4. 配置映射

k8s 允许将配置选项分离到一个名为 ConfigMap 的单独对象中。 这与秘密不同。 它习惯于不敏感的数据。 让我们展示一下。 和secret一样，有4种创建ConfigMap的方法。

- 通过 --from-literal

   >```外壳
   >kubectl create configmap myconfigmap --from-literal=config1=xxx --from-literal=config2=yyy
   >```

- 通过--from-file

   >```外壳
   >echo -n xxx > ./config1
   >echo -n yyy > ./config2
   >kubectl create configmap myconfigmap2 --from-file=./config1 --from-file=./config2
   >```

- 通过 --from-evn-file

   >```外壳
   >cat << EOF > env.txt
   >config1=xxx
   >config2=yyy
   >EOF
   >kubectl create configmap myconfigmap3 --from-env-file=env.txt
   >```

- 通过YAML文件

   >```外壳
   >apiVersion: v1
   >kind: ConfigMap
   >metadata:
   >name: myconfigmap
   >data:
   >config1: xxx
   >config2: yyy
   >```

   这和秘密是一样的。 由此，可以创建单独的config对象，然后可以在Pod中使用。

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gefemzq8dkj317a0iwdip.jpg" style="zoom:200%;" />
   
   
   
   ### 5.如何在Pod中使用configmap
   
   这和秘密是一样的。 configmap就像一个单独的对象，然后Pod可以使用该对象并获取键值。 下面是关于configmap的一种实践。
   
   - 创建配置映射。
   
      >```外壳
      >apiVersion: v1
      >kind: ConfigMap
      >metadata:
      >name: myconfigmap5
      >data:
      >logging.conf: |
      >class: logging.handlers.RotatingFileHandler
      >formatter: precise
      >level: INFO
      >filename: %hostname-%timestamp.log
      >```
   
   - 使用配置映射创建 Pod。
   
      >```外壳
      >apiVersion: v1
      >kind: Pod
      >metadata:
      >name: mypodconfig
      >spec:
      >containers:
      > - name: mypodconfig
      >   image: busybox
      >   args:
      >     - /bin/sh
      >     - -c
      >     - sleep 10; touch /tmp/healthy; sleep 30000
      >   volumeMounts:
      >   - name: foo
      >     mountPath: "/etc/foo"
      > volumes:
      > - name: foo
      >   configMap:
      >     name: myconfigmap5
      >     items:
      >       - key: logging.conf
      >         path: myapp/logging.conf
      >```
   
      在此 Pod 中，定义安装路径。 然后执行以下命令。
   
      <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gefi5lskfqj318s072dhe.jpg" style="zoom:200%;" />
