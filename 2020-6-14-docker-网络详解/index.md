# Docker网络详解


我们知道，Docker的核心是资源隔离，Docker相当于是运行在Host 主机上的一个进程，但是这些进程是如何实现彼此的互不干扰，独立运行呢？这个就要说到Docker的CGroup 和 Namespace了。

CGroup全称是Control Group，是用来设置进程使用CPU，内存和IO资源的限额。所以CGroup相当于是用来做资源的控制。Docker的CGroup配置是放在 /sys/fs/cgroup/路径下配置文件里，通过这些配置文件，来设置Docker进程的资源配置。

Namespace是实现Docker的资源隔离，分别对应了6种资源： Mount， UTS， IPC， PID，Network和 User。

-    Mount Namespace，是可以让容器能独立的拥有自己的文件系统
-   UTS Namespace， 是让容器有自己的hostname
-   IPC Namespace， 是让自己有自己独享的内存和信号量来实现进程间的通信，而不会与host和其他的容器IPC混在一起
-   PID，进程ID
-   Network namespace， 让容器拥有自己独立的网卡，IP，路由等资源。
-   User Namespace， 让容器可以管理自己的用户。

好了，说了这么多的废话，这章来讲解下容器的网络。

容器的网络实际上是分为三种，none，bridge和host。可以通过命令方式看下容器的网络配置。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs6hw545aj3138064q46.jpg" style="zoom:200%;" />

那个 my_next 是我自己配置的一个bridge网络。这个是在host docker上看到的容器网络几种类型。

### 1. none 网络

none网络就是什么都没有的网络，挂在这个网络下的就是IO，没有任何其他的网卡。可以看下。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs6lmjx06j31420aytaw.jpg" style="zoom:200%;" />

就是通过 --network=none 来配置，可以看下ifconfig就是只有local 的network。

可能有人会问，这种网络有什么作用呢，也不能和外面通信，其实还是有作用的，比如涉及到的一些隐私等可以通过这种方式配置，可以通过这个docker来生成和密钥相关的一些东西，还是非常有作用。

### 2.host 网络

这种网络配置是和Docker host共享它的网络栈，容器的网络配置与host完全一样，可以看下。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs6qvtc09j312i0b6417.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs6re4a53j31460g2tcg.jpg" style="zoom:200%;" />

可以看下，是通过--network=host 来配置网络模式是host模式。可以看到，它的网络配置主机的网络配置完全一致。

使用场景是什么呢，就是如果容器对网络传输效率有较高的要求，可以选择这种模式，但是缺点也很明显，就是不太灵活，要考虑端口冲突问题。

### 3. bridge 网络

这种是用的最多的，默认情况下就是创建的bridge网络模式。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs6w9m4i0j315205y75k.jpg" style="zoom:200%;" />

可以看到，有两个桥接网络，第一个是我手动创建的一个桥接，第二个是Docker host默认的一个桥接网络，当每用默认网络模式创建一个docker实例时，就会在默认的Docker桥接下增加一个interface。

可以创建一个桥接模式的docker试试看。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs742kep0j314s08wjth.jpg" style="zoom:200%;" />

我创建了一个Docker实例，然后在docker0的桥接下多了一个interface。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs7967nvmj31gy08oju9.jpg" style="zoom:200%;" />

可以看下这个网络配置， 网络名称是if48.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs7ckpoftj30n60860t9.jpg" style="zoom:200%;" />

这个是bridge的网络参数。同时Docker Host的ip是172.17/0.1，整个的网络模型如下所示：

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs7eh7o7tj30m60os7cm.jpg" style="zoom:67%;" />

这个就是一个bridge模式。

### 4. User-defined 网络

这个是指根据自己的需要配置docker的网络，这种就比较灵活了，docker提供了三种user-defined的网络驱动：bridge, overlay 和 macvlan。

以bridge网络为例，如果两个docker是在不同的bridge下，互相通信是肯定不行的；如果它们是属于同一个网桥下，这个时候肯定是可以的，如下图。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs7r4s5woj30o40toap3.jpg" style="zoom: 50%;" />

怎么样可以让httpd和busybox的网桥通信呢，可以在httpd容器下添加一块net_my2的网卡，通过下面的方法进行连接。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs7vi8fq5j314q09oqcn.jpg"  />

之后网络模型就如下所示了：

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs7x7ym5tj30u010w4kv.jpg" style="zoom: 40%;" />

### 5. 容器间的通信

我们知道，如果两个容器是在一个bridge下，可以互相通信，如果不在一个bridge下，可以通过docker network connect将现有容器加入到指定网格中。但是有个问题啊，我们知道容器的IP是动态变化的，不能光靠ip的方式来访问容器，可以通过网络名称方式来访问。但是这种方式只能在user-defined网络中使用，不能在默认的bridge中。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs85en8wlj31bu03s435.jpg" style="zoom: 150%;" />

### 6. joined 容器

Joined容器是另外一种实现容器通信的方式。它是使两个或多个容器共享一个网络栈，共享网卡和配置信息。

我用一个实例来演示下。

我先创建一个httpd的容器。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs8fu9tbgj30zc0200t9.jpg" style="zoom:200%;" />

然后再创建一个busybox的容器加入到web1这个容器里。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs8ghcvwcj316208wmzm.jpg" style="zoom:150%;" />

同时看下它的网络配置。我比较下web1的网络配置。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs8hcs1b7j31g008wn03.jpg" style="zoom:150%;" />

它们的网络是完全一样的。

现在在busybox的容器里直接通过127.0.0.1来访问web容器，发现是可以直接访问的，也证明了这两个容器是网络互通。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs8inrlioj30za0663za.jpg" style="zoom:200%;" />

### 7. 容器访问外部世界

我们知道，我们运行的容器是可以直接访问外网的。

![](https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs8ulsfugj30uy08umzb.jpg)

看这个，可以直接访问的。这个是怎么实现的呢。

![](https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs8wvcd35j30zy0bu417.jpg)

它是通过nat转换，将内部的网络地址转换为host的网络地址发送出去。整个过程如下图所示：

![](https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs8z0776pj316g0hcjww.jpg)

这个图非常清晰的说明了整个过程。

### 8. 外部网络访问Docker容器

外部网络访问Docker容器是通过端口映射的方式实现的，就是启动容器后，将端口映射到host的某一个端口。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs96vuud5j31z406wac4.jpg" style="zoom:200%;" />

这个就是将docker的80端口映射到了host的32768端口上，可以通过host的ip加32768端口来访问容器。

也可以在创建容器时，静态的指定端口。

![](https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs98n0379j30ws08yth0.jpg)

整个过程可以用下图来表示。

![](https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gfs99m2sttj313k0h2tfq.jpg)

整个过程是从左到右，通过docker-proxy转发给容器172.17.0.2.




