# 浅谈 lsof 的一些使用


### 1 Linux 一切皆文件
在Linux 系统中，一切皆文件。通过文件不仅可以查看存储到磁盘中的文件数据，还可以访问网络连接和硬件。问题来了，竟然一切皆是文件，那怎么通过命令方式查看及管理这些打开的文件呢。可以用lsof 命令。不仅可以查看进程打开的文件、目录，还可以查看进程监听的端口等socket 信息。

### 2 lsof 命令的常用选项
**-a** 指示其它选项之间为与的关系\
**-c** <进程名> 输出指定进程所打开的文件\
**-d** <文件描述符> 列出占用该文件号的进程\
**+d** <目录>  输出目录及目录下被打开的文件和目录(不递归)\
**+D** <目录>  递归输出及目录下被打开的文件和目录\
**-i** <条件>  输出符合条件与网络相关的文件\
**-n** 不解析主机名\
**-p** <进程号> 输出指定 PID 的进程所打开的文件\
**-P** 不解析端口号\
**-t** 只输出 PID\
**-u** 输出指定用户打开的文件\
**-U** 输出打开的 UNIX domain socket 文件\
**-h** 显示帮助信息\
**-v** 显示版本信息

### 3 一些简单的应用
这里就不列举所有的应用场景了，可以根据具体的需要再去查找，需要记住的是，但凡涉及到文件相关的，都可以想到用lsof 命令。列一些简单的应用场景，加深下对命令的使用。

#### 3.1 **查看哪些进程打开了某个文件**
这个应该是经常用到，在windowns 里比如想要关掉某个文件发现一直关不掉，原因是这个文件被很多进程同时使用了，想要把它关掉还关不掉，只能先把所有正在使用该文件的进程kill 掉才行，这时候可以用lsof 了。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/06973eb2b4514ad5af77075630136bad~tplv-k3u1fbpfcp-zoom-1.image" style="zoom:200%;" />

+d 是针对于文件夹的操作，同时如果需要kill 掉所有的进程id，可以用awk 把pid 号列下来然后kill 掉。

#### 3.2 **查看某个进程打开的所有文件**
这个有时候也需要用到，某个进程做了哪些操作，打开了哪些文件。
<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/8b897ce13cf04690ac6a4cdbaf9ee9f6~tplv-k3u1fbpfcp-zoom-1.image" style="zoom:200%;" />

用lsof -p + pid 来查看这个进程打开了哪些文件。

#### 3.3 **查看ipv4、ipv6 打开的文件**
网络相关的文件操作也是用的很多，所以对一些问题定位需要用lsof 来查看网络相关对文件的一些操作。lsof -i 是查看ipv4和v6 对文件的操作。
<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/fa82058ffef840d1aec4fe97c3fbedcd~tplv-k3u1fbpfcp-zoom-1.image" style="zoom:200%;" />
当然，如果需要单独看ipv4 或 ipv6，可以直接lsof -i ipv4/ipv6 来指定

```
$ sudo lsof -i 4
$ sudo lsof -i 6
```

#### 3.4 **列出与端口相关的文件**
这个用的就比较多了，经常要查相关端口所使用的文件，比如说22 端口或啥的。用lsof -i:port.
<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/2b7aa57bcd6c40bcb9e41ebdadf690cb~tplv-k3u1fbpfcp-zoom-1.image" style="zoom:200%;" />

### 4 具体的一个practice
之前有遇到过一个案例，就是用df -h 和 du -sh /某个文件夹， 发现两个所显示的磁盘空间占用相差很大，原因是df -h 是统计的文件夹在磁盘中空间，包括这个文件夹可能被删除过或其他地方引用着，但du 是统计的是当前文件夹实际大小，所以可能是df -h 统计的某个文件夹是大于du -sh 的。我当时就遇到这种情况，而且两者相差还非常的大，怎么解决这个问题呢，可以用lsof ｜ grep delete 来查找这个文件夹被delete 进程所占用的，然后把这些进程都kill 掉。

### 5 小结
关于lsof 的一些使用主要的就说这么多，还有很多其他的一些用法，可以根据平常工作需要来定向查找。 

可以参考： https://www.cnblogs.com/sparkdev/p/10271351.html 
