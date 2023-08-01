# 六、Volume - mount the disk to the container


### 1. volume

Finally waiting for you, volume, volume. It is also a very important component of kubernetes. No, it should not be said to be a component of k8s, it should be said to be a part of POD.

What problem is the volume used to solve? POD is actually equivalent to a logical host, and each POD may have multiple containers. We know that these containers are actually processes equivalent to logical hosts. These processes can share CPU, RAM, network, etc., but each container is With their own file systems, these systems are isolated from each other. Is there a way for these containers to share the file system? You think about this scenario, for example, a container in the POD is hung up, and then a new one is started, but this one still uses the file system resources of the previous one. How to solve this problem, do you have to use volumes, which is equivalent to using shared ones? this file system.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6x4eedbqdj30hd0fidkk.jpg" style="zoom:200%;" />

Look at this, there are three containers running in one POD, each of which is an independent file system, do you think this can run? Let me introduce these three containers, webserver, which is the entrance of the web, content is used to store web page information, and log is used to store logs. These three do not have a shared file system. When accessing, the web container cannot find the web page, nor can the log be stored. . Come on, check out the improved version.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6x4egqjntj30f70fngs5.jpg" style="zoom:200%;" />

After sharing the volume, hahaha, it's great to be able to run.



### 2. Several types of volumes

A volume is actually a storage medium, and it uses the storage medium of the host, that is, the POD host. Therefore, the performance of the volume is affected by the logical host. Of course, you can also set the volume to use memory storage. According to usage habits, there are many types of volumes. Introduce two kinds:

- [ ] emptyDir

   > It is also the simplest type of volume, and it is also the basis of other volumes. It is easy to understand that it is an empty volume. Its life cycle is consistent with the life cycle of POD. This is when the POD starts, a blank space is initialized to store the content. <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6x4ein3a0j30l10d078g.jpg" style="zoom:200%;" />
   >
   > This is an example, each image can set the path of the volume, and then the type of the volume can be set on the volume node.
   >
   > <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6x4ejucirj30ih02zdg6.jpg" style="zoom:200%;" />
   >
   > 
   >
   > This can define whether to use memory or storage media.



- [ ] Git storage volume

   > This volume is also very interesting, it is designed for git warehouse,
   >
   > This is the model diagram. When the POD starts, it will pull the remote git warehouse into this volume, but this cannot be synchronized in real time. I understand that it will not be so advanced. The prototype of the GIT volume is an empty volume, so the life cycle is consistent with that of the POD.
   >
   > ![1568261085518](<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6x4elernrj30kz09sn1k.jpg" style="zoom:200%;" />



- [ ] HostPath Volume

   > Can files be shared between PODs? Yes, this is the HostPath volume.
   >
   > <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6x4eo1yr8j30kt0abdkv.jpg" style="zoom:200%;" />
   >
   > 
   >
   > Look at this picture, two PODs share this HostPath volume, so even if you delete a POD, it will not affect this volume. But there is a problem, this volume is strongly related to POD, that is, if you use other POD, you cannot access this volume.

  

- [ ] persistent volume

   > This part is compatible with very different environments. If you are using GCP, there are corresponding component support, and other cloud platforms also have other corresponding components. So I won’t talk about this part. To figure out its usage scenario, this requires data persistence, that is, data access can be performed across different nodes. Follow-up is useful enough to focus on.
