# Linux 问题定位及性能优化


### 1.1  平均负载和CPU利用率

这两个通常是衡量系统当前性能的关键指标，但是不能只究一个而放弃另外一个，要两者一起来查看分析。

***平均负载：是指单位时间内，系统的运行状态和不可中断状态进程的个数***。

***CPU使用率：就是指CPU的使用情况，也是我们的常规理解。***

好了，细品，其实能感受到两者的一些区别，我们知道，实际上，单核CPU每一个时间点只能运行一个进程，也是最理想的状态，所以如果某一时间点，有多个进程在抢占CPU，实际上这样是不好的，平均负载会升高。不可中断状态是指那些IO进程，比如内核态下，读写硬件，这种进程，系统是不愿意中断的。

所以很好理解了，平均负载高不一定CPU利用率高，比如有很多的IO进程 ，这时候CPU利用率不一定高。而CPU利用率高，平均负载也不一定高。比如单进程中要多个线程在用CPU，这时候CPU利用率也很高，但平均负载并不高。

### 1.2 实例分析

-  ***CPU密集型进程***

  模拟一个CPU密集的进程，单个CPU的使用率达到100%，然后查看平均负载的使用情况。

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/0081Kckwgy1glcusv6mvdj30vc01w3zs.jpg" style="zoom:200%;" />

  起了一个进程，将CPU使用率调到100%，然后查看平均负载。

  我先来看看cpu的使用情况，来show几个命令的用法。

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/0081Kckwgy1glcv0cige9j310q0aiwmi.jpg" style="zoom:200%;" />

  这个是pidstat命令，可以查看进程CPU的使用，当然也可以用top命令。但是这个命令可以查看内核态和用户态的CPU占用。

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/0081Kckwgy1glcv1ul6qcj30so03eab8.jpg" style="zoom:200%;" />

  用uptime命令查看平均负载。所以可以看到，此时CPU利用率是100%，平均负载并没有很离谱。

- IO密集型进程

  模拟的是IO进程在一直运行，但是实际上cpu利用率并不会很恐怖，但是平均负载很高

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/0081Kckwgy1glcv9jqrnsj30tk03ita3.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/0081Kckwgy1glcva32ho1j310402odht.jpg" style="zoom:100%;" />

​			top 命令看不到内核态和用户态分别的系统占用，可以用pidstat 1 来查看进程的用户态和内核态占用

- 大量进程场景

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/0081Kckwgy1glcvctr4avj30uk02gq4c.jpg" style="zoom:200%;" />

  模拟的是8个进程同时运行的情况，这时候再来看看平均负载和cpu使用率。

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/0081Kckwgy1glcvf9zo9nj30ta03wgn4.jpg" style="zoom:200%;" />

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/0081Kckwgy1glcvflkw1rj310o0820zr.jpg" style="zoom:200%;" />

  可以看到平均负载很高，cpu使用率也很高。

  明白了，总结，top，一般用来查看cpu总体使用情况，当然也包括内存消耗；pidstat可以查看每个进程用户态和内核态的cpu消耗。vmstat 看io，cs，内核态和用户态的等待时间。

### 2. CPU上下文切换

CPU上下文切换是Linux系统非常重要的一个性能指标，频繁的上下文切换会影响系统的性能。啥是上下文切换呢，通俗的讲，就是当前进程或线程退出CPU时，系统会把上一个进程或线程的CPU寄存器和程序计数器保存下来，然后加载要运行的进程或线程的CPU寄存器和程序计数器，运行新任务。这一次的切换和保存是影响性能的关键。上下文切换也分为以下几种情况。

- 进程上下文切换

  进程是分为用户态和内核态，内核态是指进程要和Linux内核交互，用户态是不需要和Linux内核交互。所以进程上下文切换也分为两种情况，一种是进程由用户态转到内核态，另外一种是两个进程间的切换。

  从用户态到内核态，我们来看看这个干了啥。可以把Linux的运行等级划分为下图 ，Ring 0 是最高等级，权限也是最大，和内核直接交互。Ring 3是用户态，权限有限，只能通过系统调用的方式才能访问内核资源。

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/0081Kckwgy1glczklk45tj30m20j477t.jpg" style="zoom: 67%;" />

  从用户态到内核态的一次调用，CPU实际上是做了两次上下文切换，第一次是将用户态的指令位置保存起来，执行内核代码，更新内核指令，跳到内核执行；执行完后，恢复到用户态，是CPU寄存器恢复原来保存的用户态，然后再切换到用户空间。所以发生了两次上下文切换。

  进程间内核态的上下文切换相对于系统调用，要保存的消息会更多，比如CPU的进程从一个切换到另外一个，不仅要保存CPU寄存器和程序计算器，同时还要保存虚拟内存、栈等。所以资源消耗和时间会更多。

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/0081Kckwgy1glczr1jr93j30y006m3z9.jpg" style="zoom:200%;" />

- 线程上下文切换

  线程是运行于进程的任务，如果进程中只存在1个线程，线程切换可以认为是进程间的 切换 。当进程中有多个线程时，因为多个线程是共享进程的虚拟内存和全局变量的 ，所以一次线程间的切换，CPU只用保存线程的私有数据、寄存器和不共享的资源，所以线程间切换要比进程间切换效率高很多。

- 中断上下文切换

  中断进程的优先级是高于普通进程的，而且中断进程是发生在内核态，所以中断进程打断了用户态的进程，不用保存和恢复这个进程的虚拟内存、全局变量等用户资源。中断上下文，其实只包括内核态中断服务程序执行所需的状态，包括CPU寄存器、内核堆栈、硬件中断参数等。

### 3. 不可中断和僵尸进程

先来回顾下进程的几种状态，这个在平时分析查看时要经常看的。

***R：运行状态进程***

***D：不可中断状态进程，一般是进程在和硬件交互时，不允许交互过程被其他进程或中断打断***

***Z：僵尸状态。这种是子进程退出后，父进程没有回收子进程，导致处于僵尸状态。一般父进程有一个wait函数来回收子进程的状态***

***S：可中断状态进程。表示进程因为等待某个事件被系统挂起，可以被唤醒进入就绪和运行状态***

***T：暂停状态，就是比如进程在运行时，发送一个SIGSTOP信号后，进程处于暂停状体啊，可以通过fg命令恢复***

***I：处于空闲状态***

所以在进行系统分析时，如果有大量的不可状态进程，也就是D状态进程，就要考虑系统的IO问题了。

而对于僵尸进程，正常情况下，并不会影响系统的性能，但是如果大量僵尸进程，可能会把系统的PID号占用完，僵尸进程的清理，可以杀掉父进程 或者等init进程回收。

### 4. 分析CPU的性能指标

这个也是实操部分最关键的，就是出现CPU问题了，可以从哪些角度去分析，第一，肯定是CPU使用率，CPU使用率又包括用户CPU，内核CPU，等待IO，中断，窃取CPU，客户CPU。第二，就是上下文切换。第三，就是平均负载。第四，CPU缓存的命中率。CPU和内存之间是有缓存，通常会把热点数据写到缓存中，缓存的命中率能很大程度提高CPU的性能。

来简单说下自愿和非自愿的上下文切换。

***自愿上下文切换：是指进程无法获取所需资源，导致的上下文切换。比如IO，内存等资源不足。***

***非自愿上下文切换：进程间时间片已用完，被系统强制调度，进而发生的上下文切换***

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/0081Kckwgy1gld2oxrf6dj31100rmdi9.jpg" style="zoom:200%;" />



### 5. 工具

![](https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/0081Kckwgy1gld2z4enlhj30ul0u0n7x.jpg)



<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/0081Kckwgy1gld2zqvozqj30rs0yitjx.jpg" style="zoom:200%;" />




