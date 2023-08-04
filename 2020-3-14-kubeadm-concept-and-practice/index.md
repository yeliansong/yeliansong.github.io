# kubeadm 概念与实践


### 1.kubeadm知识图谱

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/00831rSTgy1gctptvfodzj318m0min0y.jpg" style="zoom:200%;" />

Kubeadm是一个快速实现k8s环境的工具。 另外，您不需要关心配置环境，只需知道如何引导它即可。 掌握使用 kubeadm 的基本命令。


### 2.Kubeadm实践

#### 2.1 练习环境

谷歌云实例
Linux系统。

#### 2.2 环境配置

* 安装容器（Docker）

   > ```
   > # 安装 Docker CE
   > ## 设置仓库
   > ### 安装软件包以允许 apt 通过 HTTPS 使用存储库
   > apt-get update && apt-get install \
   > apt-transport-https ca-certificates curl software-properties-common
   > 
   > ### 新增 Docker 的 官方 GPG 秘钥
   > curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
   > 
   > ### 添加 Docker apt 仓库
   > add-apt-repository \
   >  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \                             
   >      $(lsb_release -cs) \                                                                 
   >      stable"
   > 
   > ## 安装 Docker CE
   > apt-get update && apt-get install docker-ce=18.06.2~ce~3-0~ubuntu
   > 
   > # 设置 daemon
   > cat > /etc/docker/daemon.json <<EOF
   > {
   > "exec-opts": ["native.cgroupdriver=systemd"],
   > "log-driver": "json-file",
   > "log-opts": {
   > "max-size": "100m"   
   > },
   > "storage-driver": "overlay2"
   > }
   > EOF
   > mkdir -p /etc/systemd/system/docker.service.d
   > 
   > # 重启 docker.
   > systemctl daemon-reload
   > systemctl restart docker
   > ```

* 安装 kubeadm、kubectl 和 kubelet

   >```
   >apt-get update && apt-get install -y apt-transport-https curl
   >curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
   >
   >cat <<EOF >
   >/etc/apt/sources.list.d/kubernetes.list
   >deb https://apt.kubernetes.io/ kubernetes-xenial main
   >EOF
   >
   >apt-get update
   >
   >apt-get install -y kubelet kubeadm kubectl
   >apt-mark hold kubelet kubeadm kubectl
   >```

#### 2.3 kubeadm 实践

背景：使用kubeadm创建k8s主节点，然后将其他节点循环到该主节点。

* 初始化主节点。

   > ```bash
   > kubeadm init --pod-network-cidr=10.244.0.0/16 --ignore-preflight-errors=all
   > ```

   pod-network-cidr，表示识别pod ip范围，我们也使用flannel网络设计方案。
   忽略，表示忽略启动时的错误。 因为在启动kubeadm的时候，可能会碰到硬件不舒服。

* 启动成功后，会生成kubeadm token，该token可以用来加入其他节点。 您可以使用以下命令来查看令牌。

   > ```bash
   > kubeadm token list
   > ```

  


- 配置 kubectl。

   众所周知，kubectl是控制kubernetes集群的命令工具。 当我们切换到master节点时，我们需要配置kubectl。

   > ```bash
   > mkdir -p $HOME/.kube
   > cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
   > chown $(id -u):$(id -g) $HOME/.kube/config
   > echo export KUBECONFIG=~/.kube/config>> ~/.bashrc
   > source ~/.bashrc
   > ```


- 安装 Pod 网络插件。 安装 Pod 网络后，Pod 之间可以相互通信。 我们也使用flannel网络模式。

   > ``` 重击
   > kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/2140ac876ef134e0ed5af15c65e414cf26827915/Documentation/kube-flannel.yml
   > ```

- 将其他节点加入集群。

   > ``` 重击
   > sudo kubeadm join 10.128.0.2:6443 --token 5dhzcw.h7aih16mg982ms2o --discovery-token-ca-cert-hash sha256:e9e6843a6ae6fc5fb8acb9f116bc58d1c1e0f30d1da9bfe3bf151319c3788d57 --ignore-preflight-errors=all
   > ```

- 清理环境。
   部署后，您可以清理环境。

     > ```bash
     > sudo kubeadm reset
     > ```

### 3.附加

事实上，当你按照步骤去做的时候，会出现很多问题。
未解决的问题：

* 执行kubeadm join命令后，终端显示添加成功，但实际上节点列表中并不存在新节点。
   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/00831rSTgy1gctpsng90mj326w0t6gx6.jpg" style="zoom:200%;" />



   解决方案：我误解了kubeadm的概念，所以碰到了这个问题。
   实际上，kubeadm 的目的是创建实现 k8s 环境，因此当您执行 kubeadm init 命令时，它会创建 kubenetes 主节点。 然后就可以将其他节点安排到这个主节点上。 所以我的解决方案是这样的。

   首先，创建一个新实例，然后在该实例中配置容器、kubectl、kubelet 和 kubeadm 工具。 之后，执行此命令。

   > ```
   > kubeadm join --token 5dhzcw.h7aih16mg982ms2o 10.128.0.2:6443 --discovery-token-ca-cert-hash sha256:e9e6843a6ae6fc5fb8acb9f116bc58d1c1e0f30d1da9bfe3bf151319c3788d57 --ignore-preflight-errors=all
   > ```

   当然，您必须是 root 角色。 结果如下。

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/00831rSTgy1gcupzi3schj30vc03ymy7.jpg" style="缩放:200%;" />

  

- 在节点机器中，当您执行命令“kubectl version”或“kubectl getnodes”时，会遇到此问题。

   <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/00831rSTgy1gd2sn8gkg0j31de032jsa.jpg" style="zoom:200%;" />

   您可以下载主节点“/etc/kubernetes/admin.conf”，然后将此文件复制到节点机器路径“/etc/kubernetes/”。 然后按照前面的步骤配置 kubectl。

### 4.参考链接

- 如何安装泊坞窗。

    [https://kubernetes.io/docs/setup/生产环境/container-runtimes/#docker](https://kubernetes.io/docs/setup/生产环境/container-runtimes/#docker)



- 如何安装 kubectl、kubeadm、kubelet。

    [https://kubernetes.io/docs/setup/product-environment/tools/kubeadm/install-kubeadm/#installing-kubeadm-kubelet-and-kubectl](https://kubernetes.io/docs/setup/ 生产环境/工具/kubeadm/install-kubeadm/#installing-kubeadm-kubelet-and-kubectl)



- 练习指导。

    [https://kubernetes.io/docs/setup/生产环境/tools/kubeadm/create-cluster-kubeadm/](https://kubernetes.io/docs/setup/生产环境/tools/kubeadm/ 创建集群-kubeadm/)
