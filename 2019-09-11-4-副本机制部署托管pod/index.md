# 四、副本机制部署托管POD

### 1. 存活探针

为啥要搞出这么一个高深的词？我们知道POD里如果有容器程序崩溃了，kubenetes 会重新启动程序，但是问题来了，如果不是崩溃的情况呢，比如死锁了，或者抛了异常等等，这个时候咋整，kubenetes也不知道你的容器是否正常，这个时候就要用到探针了。其实道理很简单，就是用一个探针时不时地探测下，看是否正常。

三种探针：1）HTTP GET探针，就是用来检查网络是否正常。2）TCP套接字探针，也差不多，就是建立TCP连接，如果成功了就是正常的。3）Exec探针，就是在容器内执行任意命令，如果返回正常就是成功的。

探针其实也是一个POD，可以定义一些属性，用来控制探针的一些操作。



### 2. ReplicationController

也是一个很牛逼得东西，就是副本控制吧。就是用来保证POD的个数，可用来POD的水平扩展。

RC 有三个部分：label selector,标签选择器，用来确定RC作用域有哪些POD； RC COUNT：用来指定POD的数量； POD TEMP：模板，创建新POD副本。

来看看标签对RC的影响。其实也很好理解，RC只对它里面定义的标签负责，时刻监控着这些标签的POD个数，当这些标签的POD有减少或增加时，会动态调整。所以呢，两种情况，第一种，如果你修改了运行的POD里的标签，相当于这个POD以前是属于A，然后后面属于B了，这个时候RC要干事了，他会重新来创建POD。第二种情况，修改RC的标签，那这个标签里的POD全部脱离监控，全部都是自由的。

是用kubectl edit rc kubia 玩玩，你会发现，你可以修改当前的RC，然后修改当前的RC对现在运行的POD是没有任何影响的，只会对后面的POD有影响。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6vz9qkq36j30h90ab76n.jpg" style="zoom:200%;" />

有点意思，三个POD，删除RC后，这3个POD不受影响，脱离了RC的束缚。

but， 不要用RC了，用ReplicaSet, 这哥们的功能和RC一样，但是功能增强了很多，主要是对标签的运用上更加灵活，其他的和RC完全一样，所以对这个也不要有压力了。



### 3. DaemonSet 

这个又是用来干啥的呢，是用来控制POD的部署，意思就是按照自己的定义来部署POD。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6vz9rj59cj30mc0d4jxi.jpg" style="zoom:200%;" />

来来来，看这货，左边是用的ReplicaSet，部署的POD在每个节点上是杂乱无章的，我现在要求每个节点只部署一个POD，这种情况怎么处理？这就要用到DaemonSet了。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6vz9shyq4j30jr0acdhl.jpg" style="zoom:200%;" />

这个时DaemonSet的YAML 文件，nodeSelector 节点调度器。



### 4. JOB

这个是用来定义一次任务，就是在完成后结束掉。而不是希望一直在运行它，这个也是一个很好的运用。JOB也有很多应用设置，可以设置任务的延迟时间等。


