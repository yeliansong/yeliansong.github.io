# 一次由iNode 引发的惨案，爆肝四小时终于理解了iNode


## 1 背景

一次在做程序包变更时，程序包已经更新到最新版本，需要重启进程，就一直重启不成功。查看启动的错误日志，发现是一直在创建文件时不成功，当时想法是机器磁盘可能满了，查看磁盘使用，发现正常，瞬时就懵逼了，一直想不到是啥问题。突然想到之前有了解过Linux 系统有inode 一说，中文译名是：索引节点。创建的每一个文件都有一个inode，这个inode是用来记录文件的基础信息，这个节点资源也是有限的，马上去查了下，发现inode占用已经100% 了，这完犊子了，马上清理，问题解决。这篇就来说说这个吧。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/5c8980c1815a4eb0ae95789acf79f895~tplv-k3u1fbpfcp-zoom-1.image" style="zoom:200%;" />

<br>

## 2 iNode 的理解

### 2.1 磁盘存储
要想理解iNode，首先得需要知道Linux 的磁盘存储的一些知识。Linux 磁盘的最小的存储单位是片区，就是sector,一般一个扇区的大小是512 bytes，操作系统读取数据时候不是以扇区为单位来读，这样就太慢了，而是以块来读取，也就是block，一个block 会有多个sector，一般一个block 是4KB，8个sector。这8个sector 是连续的。操作磁盘命令是 fdisk。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/008i3skNgy1gytdh0f62xj30hr08zdgs.jpg" style="zoom:200%;" />

可以看到磁盘的分区、分区大小、sector、block 等相关的信息。okay，说了这么多，其实需要知道的一个信息是文件存储的最小单位是 block，那这个和iNode 有什么关系呢？

### 2.2 iNode 的内容
先来看看iNode 中存的信息有哪些？
我随便开一个文件，看看这个文件的iNode 信息：
<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/008i3skNgy1gytdpo2nvlj30kr03t3yt.jpg" style="zoom:200%;" />

```txt
- File: 文件
- Size: 文件的大小
- Block: 所属的块 编号
- Gid: 文件的Group ID
- A M C: 文件的时间戳，分别上次访问、文件修改、iNode 修改的时间戳
- Inode: 文件的Inode 值
- Links: 文件的链接数
```
看这个iNode 内容，就不难理解iNode 的作用了。可以理解为操作系统给创建的每一个文件一个iNode 节点，也就每个文件和iNode 号是一个map关系，存储时候这个iNode 号才是关键。当需要对该文件操作时，分为三步：**1）通过文件名找到iNode 节点号。 2） 通过iNode 节点号获取整个iNode 信息。3）根据iNode 信息找到文件所属的Block，读出数据。** 可以通过ls -i 来看文件的iNode 号。
<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/008i3skNgy1gyte6aho91j30nr00zt8k.jpg" style="zoom:200%;" />

### 2.2 iNode 大小
iNode 也是会消耗硬盘空间的，硬盘格式化后会分为两个区，一个是数据区，存放文件数据；另一个是iNode 区，用来存放iNode 所包含的信息。每个iNode 大小一般是128字节或256字节，可以用dumpe2fs 命令来查看iNode 大小。
<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/008i3skNgy1gytfxo5fuwj30j502vaa4.jpg" style="zoom:200%;" />

同时系统分配的iNode 节点个数是有限的，所以很有可能发生iNode 节点用完的情况，用完后，就无法在硬盘上创建新的文件了。所以就发生了文章开头的事情。关于iNode 写完后怎么清理，看下面文章描述。

### 2.4 iNode 含义小结
通过介绍，可以看出iNode 的Linux 设计哲学，Linux 是一切皆文件，而文件的标识就是iNode，所以文件名对于Linux 系统来说就不重要了，重要的是独一无二的iNode，有了iNode 节点号，就能准确的找到Linux 里的所有文件。

<br>

## 3 iNode 的延伸

### 3.1 目录文件权限
文件都是在目录中，在Linux系统中，目录也是一种文件，打开目录实际上就是打开目录下的文件。目录文件就是目录下文件名和iNode 节点信息的集合。
<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/008i3skNgy1gytg3y7g6rj30js01s0so.jpg" style="zoom:200%;" />
读取文件的iNode 节点是需要执行权限，通过这个就很容易理解目录权限和文件权限的关系了。
如果目录没有执行权限，基本啥都干不了，不能读取目录下文件的一些信息，执行权限对于目录权限来说是至关重要的。
<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/008i3skNgy1gytgax9egoj30mw02l0ss.jpg" style="zoom:200%;" />

root 权限除外哈，root 权限基本就是超人，内裤外穿，不受任何影响。

### 3.2 硬链接
有了iNode 的理解，对Linux 里的一些链接的理解和使用也就比较容易了。
上面说过，一般情况下一个文件名和一个iNode 号是一一对应关系，但是也可以多个相同的文件名对应一个iNode 号。这样就可以用不同的文件名来访问同样的内容，对文件内容修改会影响到所有指向这个iNode 的文件；但是删除一个文件吗文件，不会影响另一个文件对这个iNode 的访问。这就是用的很多的硬链接。
掌握了iNode，对硬链接也比较容易理解，文件的实际内容只和iNode 节点有关，和文件名没关系。
<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/008i3skNgy1gytgpa2wwaj30lx04daah.jpg" style="zoom:200%;" />

我创建了一个test.txt 的一个硬链接，可以看到这两个文件的iNode 值是一样的。也可以看到链接数是2，如果删除其中一个文件，链接数会减1，只到为0 后就会回收这个iNode 号码。

这里说明下目录的iNode，创建目录后，默认会生成两个目录：‘.' 和 ‘..’。前者的iNode 号码就是当前目录的iNode 号码，后者的iNode 号码是当前目录的父目录的iNode 号码。


### 3.3 软链接
还有一种是软链接，也叫符号链接，它是两个文件A 和 B的iNode 不一样，但是文件A 的内容是文件B 的路径，系统会自动将访问指向B，所以无论打开哪个文件，都是操作的的文件B。
<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/008i3skNgy1gyth6y084wj30js028glq.jpg" style="zoom:200%;" />

所以文件A 是依赖于文件B，如果删除了文件B，文件A 也就打不开了。这个和硬连接的区别是，文件A 指向的是文件B 的文件名，而不是文件B 的iNode 号码。

<br>

## 4 iNode 资源耗尽的解决

回到文章开头的问题，通过df -i 看，我的iNode 使用已经是100% 了，怎么解决呢？
基本思路就是找文件句柄在哪个路径下，一般iNode 耗尽肯定是有进程或任务一直在创建文件，导致耗尽。

1） 查看文件最多的目录
```shell
for i in /*; do echo $i; find $i | wc -l; done
```
如果确定哪个目录，可以吧/* 写的具体点。

2） 删除大量文件
```shell
ls | xargs -n 1000 rm -rf
```
删除就可以了，用xargs 命令。

找到问题后要避免这种大量创建文件的问题。
