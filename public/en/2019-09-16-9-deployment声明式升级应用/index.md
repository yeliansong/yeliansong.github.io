# 九、Deployment declarative upgrade application


### 1. Several ways to upgrade

Let's look at a case first, how to deal with this situation:

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g71nmdt0vuj30g608h3ze.jpg" style="zoom:200%;" />

The POD is currently using the V1 version, and now there is a V2 version, how to replace the V2 version with the V1 version? There are three ways:

- [ ] Delete the old version POD and replace it with the new version POD

   > <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g71nmgk8eaj30le0c10yd.jpg" style="zoom:150%;" />
   >
   > This method is more violent. It is to directly modify the configuration template of V1 to V2, and then delete the POD of V1. At this time, the template of V2 will be detected. If there is no POD, the POD of V2 version will be restarted. One problem with this approach is that the entire service stops when V1 is deleted.



- [ ] blue-green deployment

   > <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g71nmiqr20j30ls0a1gqg.jpg" style="zoom:200%;" />
   >
   > This is like this, that is, your program supports V1 and V2 versions at the same time, and your environment resources are sufficient to run these two at the same time. How to do it? It is to start the V2 POD in your environment. After everything is ok, you can delete the V1 POD and switch the service traffic to V2. The problem with this method is that the resource overhead is relatively large.



- [ ] rolling upgrade

   > ![222](https://p.ipic.vip/40bi67.jpg)
   >
   > This is more powerful. It uses capacity expansion and contraction to realize dynamic replacement and upgrade. What do you mean, is to define the old and new versions of PODs in your deployment file, and then delete the V1 PODs in turn to dynamically expand the V2 PODs. But in this way, if you use commands to operate, it is more cumbersome.



### 2. Use ReplicationController to realize automatic rolling upgrade

Use the kubectl command to perform rolling upgrades. kubectl rolling-update kubia-v1 kubia-v2 --image=luksa/kubia:v2 command.

What exactly does this command do? Let's see.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g71nmmv5gvj30j506ojt3.jpg" style="zoom:200%;" />

<img src="https://p.ipic.vip/lpzdzr.jpg" alt="444" style="zoom:200%;" />

You can look at this picture, which is to gradually replace the POD of V1 with V2 by modifying the number of Replicas. But there is a problem with this method, because the Kubectl method is used to complete these, which is equivalent to the client method, so if there is no network, the upgrade may stop.



### 3. Use Deployment to upgrade the application

Deployment is a more advanced upgrade method. It is an upgrade method belonging to the upper layer, while the other types belong to the bottom layer.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g71nmqdl59j30hu03k0ta.jpg" style="zoom:200%;" />

When using Deployment, ReplicaSet is actually used to manage POD. So how do you do rolling upgrades?

Deployment is a deployment file, in which you can define the information you want to deploy, and then deploy.

![](https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g71nms17isj30jf08jac2.jpg)

A deployment is defined, now let's see how to implement a rolling upgrade. First, the upgrade needs to be triggered. How to trigger it? It is triggered by modifying the Deployment file. You can use Kubectl set image deployment kubia nodejs=luksa/kubia:v2 to re-specify the image, and the POD will download the image again.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g71nmtibo8j30ll08agoq.jpg" style="zoom:200%;" />

Then internally, it will delete the POD of V1 in turn, and then start the POD of V2. It can also define its own upgrade strategy, RollinUpdate and Recreate, the default is the first.



### 4. Rollback upgrade

Now there is a problem, if you want to upgrade a V3 version, but there are some bugs in the V3 version, you upgrade, and then find that there is a problem, how to go back to the previous version? It can be solved by command: kubectl rollout undo deployment kubia, you can roll back to the previous version. You can also roll back to a certain historical version. You can view the history first: kubectl rollout history deployment kubia to view all historical versions, and then use kubectl rollout undo deployment kubia --to-revision = ? to roll back to a certain version.



### 5. State control of rolling upgrade

- [ ] Control upgrade rate

   > It is defined with two parameters: maxSurge and maxUnavailable. I don’t really want to figure out how to calculate it. You can look at the effect.
   >
   > <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g71nmum3dkj30ll08agoq.jpg" style="zoom:200%;" />



- [ ] Pause rolling upgrade

   > This can be used to play canary upgrades. What is a canary is bound. How to play, is to do a rolling upgrade first, and then immediately suspend the rolling upgrade. At this time, a new POD will be created, the old POD is still running, and some traffic will be switched to the new POD, and then test, test After passing, you can resume the rolling upgrade, complete the replacement, and if the test fails, you can roll back to the previous version. The canary upgrade is actually to let some people experience the new version. Take a look at the command:
   > kubectl rollout pause deployment kubia
   > kubectl rollout resume deployment kubia



- [ ] Prevent rolling upgrades of buggy versions

   > There is another better way, which is to set a time period and set the probe. During this time period, if there is no problem with the new POD, rolling upgrade is supported. This is equivalent to setting up an insurance that can minimize the risk.



- [ ] The deadline configured for rolling upgrades

   > It is to set a time period. If the program is not upgraded successfully, the upgrade can be canceled.
