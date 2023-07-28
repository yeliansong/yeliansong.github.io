# 五：POD的服务与通信




###  1. 服务与端口

服务其实很好理解了，你想想看，一组相同的POD，你怎么管理，你需要知道他们的所有IP吗，然后再去一一进行手动配置连接？显然不需要的，怎么解决这个问题呢，就用服务，服务其实就是相当于一个路由的功能。

![1568172108504](https://tva1.sinaimg.cn/large/006y8mN6gy1g6vz9tf8wej30mf0dnq60.jpg)

看看这个，前端有3个POD，还有一个Backend，怎么使整个系统正常运行呢，使用服务。三个前端设置一个前端服务，暴露一个IP，Backend也一样，暴露一个服务，所以每一部分的连接就只关注这个服务IP，而不用管每个POD的网络信息了。

![1568172261841](https://tva1.sinaimg.cn/large/006y8mN6gy1g6vz9trl8vj30i707bjsq.jpg)

这个是创建服务的YAML，KIND是一个Service， 然后将POD的端口进行映射，还有一个标签选择器。可以用kubectl expose 或 kubectl create 来创建服务。

![1568172425531](https://tva1.sinaimg.cn/large/006y8mN6gy1g6vz9ubj81j30px0dwn2q.jpg)

这个好玩吗， 就是通过服务的方式来测试是否可以访问POD。就是先exec到一个POD中，然后通过curl方式来访问这个服务的ip，看能否连接到其他的POD。 很简单了。           

来说说端口，一个POD可以有一个端口，也可以有多个端口，好理解了。



### 2. 服务发现

其实就是用环境变量的方式来连接这个服务，而不是用固定IP的方式，毕竟IP可能会有变化。 可以选择一个POD，然后kubectl exec kubia-3inly env 来列出环境变量，然后查看这个服务的环境变量，通过变量的方式供给其他客户端连接。



### 3. Endpoint

这家伙比较有意思了。看图吧。

![1568189555390](https://tva1.sinaimg.cn/large/006y8mN6gy1g6vz9v2ldhj30sm0c67e1.jpg)

很清晰明了，相当于把服务映射到了两个Endpoint中，可以理解为是负载均衡吗，有点像。



### 4. 服务暴露给外部客户端的方法

记住了，三种方法。

- [ ]  NodePort 

	>  不知道这个设置的意义，啥意思呢，就是相当于给所有的节点预留了一个PORT，然后呢你有两种途径来访问它。第一种是clusterIp:端口，第二种是nodeIp：端口  ![1568193172704](https://tva1.sinaimg.cn/large/006y8mN6gy1g6vz9w5kr5j30kl08hac7.jpg)有三个端口号，第一个是服务集群的端口，第二个是POD的目标端口，第三个是nodePort端口。![1568193758894](https://tva1.sinaimg.cn/large/006y8mN6gy1g6vz9x1ii4j30pg0j845q.jpg)这个图可以看到，30123是nodeport的端口，通过这个端口加node的IP可以访问节点。

- [ ]  负载均衡方式

	> 它是从云基础架构中，搞一个外部IP，这个IP是独一无二的可公开访问的IP地址，通过这个再重定向到服务。其他的感觉没啥说的，看这个吧。
	>
	> ![1568194400337](https://tva1.sinaimg.cn/large/006y8mN6gy1g6vz9y0p7gj30ew06vmyh.jpg)这个负载均衡器可以平均流量，看看它的策略。

- [ ]  ingress

	> 一图看清它的功能：
	>
	> ![1568195843695](https://tva1.sinaimg.cn/large/006y8mN6gy1g6vz9yhuk1j30p808oadh.jpg)啥意思呢，就是说可以通过域名的方式来选择性的访问服务。
	>
	> ![1568195964547](https://tva1.sinaimg.cn/large/006y8mN6gy1g6vz9yz6fkj30nb0aswji.jpg)这张图是看通过ingress方式来访问POD。

	

### 5. 就绪探针

又他妈的一个神奇东西。真的是要处理各种情况，就绪探针是用来处理这种情况，就是你启动一个POD，不可能立即马上就起来吧，但是kube不知道啊，它可能还是会把流量可能给你啊，所以怎么避免这个问题呢，就用到了就绪指针，就是说，设置一个指针，成功或失败了都通知kube。

![1568196997031](https://tva1.sinaimg.cn/large/006y8mN6gy1g6vzg9qd9bj30hz0baabc.jpg)

设置了一个就绪指针，就是在容器中执行ls命令，看文件存不存在。




